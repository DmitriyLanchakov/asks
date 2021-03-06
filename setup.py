#!/usr/bin/env python3

from setuptools import setup
from sys import version_info

ver = version_info[:2]
if ver < (3, 6):
    raise SystemExit('Sorry! asks requires python 3.6.0 or later.')

setup(
    name='asks',
    description='asks - async http',
    long_description='asks is an async http lib for curio',
    license='MIT',
    version='0.2.1',
    author='Mark Jameson - aka theelous3',
    url='https://github.com/theelous3/asks',
    packages=['asks'],
    install_requires=['curio', 'h11'],
    classifiers=['Programming Language :: Python :: 3']
)
