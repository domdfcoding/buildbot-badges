#!/usr/bin/env python3
#
#  __init__.py
"""
Fork of buildbot-badges with support for specifying builders by name.
"""
#
#  Copyright Buildbot Team Members
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 2
#  as published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# stdlib
from typing import Any, Dict
from xml.sax.saxutils import escape

# 3rd party
import buildbot.master  # type: ignore
import cairocffi as cairo  # type: ignore
import cairosvg  # type: ignore
import jinja2
from buildbot.process.results import Results  # type: ignore
from buildbot.util import bytes2unicode  # type: ignore
from buildbot.www.plugin import Application  # type: ignore
from klein import Klein  # type: ignore
from twisted.internet import defer

__author__: str = "Buildbot Team Members"
__copyright__: str = "2020 Dominic Davis-Foster"
__license__: str = "GNU General Public License v2 (GPLv2)"
__version__: str = "2.9.4"
__email__: str = "users@buildbot.net"

__all__ = ["Api"]

color_scheme: Dict[str, Any] = {
		"exception": "#007ec6",  # blue
		"failure": "#e05d44",  # red
		"retry": "#007ec6",  # blue
		"running": "#007ec6",  # blue
		"skipped": "a4a61d",  # yellowgreen
		"success": "#4c1",  # brightgreen
		"unknown": "#9f9f9f",  # lightgrey
		"warnings": "#dfb317"  # yellow
		}


class Api:  # noqa: D101
	app = Klein()

	default = {  # note that these defaults are documented in configuration/www.rst
		"left_pad": 5,
		"left_text": "Build Status",
		"left_color": "#555",
		"right_pad": 5,
		"border_radius": 5,
		"style": "plastic",
		"template_name": "{style}.svg.j2",
		"font_face": "DejaVu Sans",
		"font_size": 11,
		"color_scheme": color_scheme,
	}

	def __init__(self, ep):
		self.ep = ep
		self.env = jinja2.Environment(
				loader=jinja2.
				ChoiceLoader([jinja2.PackageLoader("buildbot_badges"), jinja2.FileSystemLoader("templates")])
				)

	def makeConfiguration(self, request):  # noqa: D102

		config = {}
		config.update(self.default)
		for k, v in self.ep.config.items():
			if k == "color_scheme":
				config[k].update(v)  # type: ignore
			else:
				config[k] = v

		for k, v in request.args.items():
			k = bytes2unicode(k)
			config[k] = escape(bytes2unicode(v[0]))
		return config

	@app.route("/<path:builder>.png", methods=["GET"])
	@defer.inlineCallbacks
	def getPng(self, request, builder):  # noqa: D102
		svg = yield self.getSvg(request, builder)
		request.setHeader("content-type", "image/png")
		defer.returnValue(cairosvg.svg2png(svg))

	@app.route("/<path:builder>.svg", methods=["GET"])
	@defer.inlineCallbacks
	def getSvg(self, request, builder):  # noqa: D102

		master: buildbot.master.BuildMaster = self.ep.master

		if not builder.isidentifier():
			builder = yield master.db.builders.findBuilderId(builder, False)

		config = self.makeConfiguration(request)
		request.setHeader("content-type", "image/svg+xml")
		request.setHeader("cache-control", "no-cache")

		# get the last build for that builder using the data api
		last_build = yield self.ep.master.data.get(("builders", builder, "builds"), limit=1, order=["-number"])

		# get the status text corresponding to results code
		results_txt = "unknown"
		if last_build:
			results = last_build[0]["results"]
			complete = last_build[0]["complete"]
			if not complete:
				results_txt = "running"
			elif results >= 0 and results < len(Results):
				results_txt = Results[results]

		svgdata = self.makesvg(results_txt, results_txt, left_text=config["left_text"], config=config)
		defer.returnValue(svgdata)

	def textwidth(self, text, config):
		"""
		Calculates the width of the specified text.
		"""

		surface = cairo.SVGSurface(None, 1280, 200)
		ctx = cairo.Context(surface)
		ctx.select_font_face(config["font_face"], cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
		ctx.set_font_size(int(config["font_size"]))
		return ctx.text_extents(text)[4]

	def makesvg(self, right_text, status=None, left_text=None, left_color=None, config=None):
		"""
		Renders an SVG from the template, using the specified data.
		"""

		right_color = config["color_scheme"].get(status, "#9f9f9f")  # Grey

		left_text = left_text or config["left_text"]
		left_color = left_color or config["left_color"]

		left = {"color": left_color, "text": left_text, "width": self.textwidth(left_text, config)}
		right = {"color": right_color, "text": right_text, "width": self.textwidth(right_text, config)}

		template = self.env.get_template(config["template_name"].format(**config))
		return template.render(left=left, right=right, config=config)


# create the interface for the setuptools entry point
ep = Application(__name__, "Buildbot badges", ui=False)
ep.resource = Api(ep).app.resource()
