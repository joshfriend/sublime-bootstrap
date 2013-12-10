#!/usr/bin/env python

"""
Setup script for ArniePye.
"""

import sys

import setuptools

from sublimebootstrap import __project__

CLI = 'sbs'
# Append the Python main version number to the end of the CLI name
CLIN = CLI + str(sys.version_info[0])


setuptools.setup(
    name=__project__,
    version='0.0.1',

    description="A small program to easily set up a Sublime Text project file..",
    url='http://arnie/pypi/ArniePye',
    author='Josh Friend',
    author_email='josh@fueledbycaffeine.com',

    packages=['sublimebootstrap'],
    package_data={'sublimebootstrap': ['data/*']},

    entry_points={'console_scripts': [CLI + ' = sublimebootstrap:main',
                                      CLIN + ' = sublimebootstrap:main']},

    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read(),
)
