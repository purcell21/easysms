""" Setup EasySMS """

import os

from setuptools import setup, find_packages
import re


MODULE_NAME = 'easysms'
PACKAGE_DATA = list()


def _read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

_meta = _read('easysms/__init__.py')
_license = re.search(r'^__license__\s*=\s*"(.*)"', _meta, re.M).group(1)
_project = re.search(r'^__project__\s*=\s*"(.*)"', _meta, re.M).group(1)
_version = re.search(r'^__version__\s*=\s*"(.*)"', _meta, re.M).group(1)
_author = re.search(r'^__author__\s*=\s*"(.*)"', _meta, re.M).group(1)
_email = re.search(r'^__email__\s*=\s*"(.*)"', _meta, re.M).group(1)

setup(
    name=_project,
    version=_version,
    description=_read('DESCRIPTION'),
    long_description=_read('README.md'),
    license=_license,

    author=_author,
    author_email=_email,
    url="https://github.com/sv0/easysms",
    keywords='easysms sms heroku',
    packages=find_packages(),
    package_data={'': PACKAGE_DATA, },
)