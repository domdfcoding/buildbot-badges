#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import pathlib
import shutil
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

extras_require = {}

repo_root = pathlib.Path(__file__).parent
install_requires = (repo_root / "requirements.txt").read_text(encoding="UTF-8").split('\n')

setup(
		description="Fork of buildbot-badges with support for specifying builders by name.",
		extras_require=extras_require,
		install_requires=install_requires,
		name="buildbot-badges",
		py_modules=[],
		)

shutil.rmtree("buildbot_badges.egg-info", ignore_errors=True)
