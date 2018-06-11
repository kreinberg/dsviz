#!/usr/bin/env python


import io
import re
from setuptools import setup


with io.open('./README.rst', 'rt', encoding='utf-8') as f:
    readme = f.read()

author      = 'Jason Kreinberg'
version     = '0.0.1'
description = ''

setup(
    name='dsviz',
    version=version,
    license='MIT',
    author=author,
    description=description,
    long_description=readme,
    platforms='any',
    packages=['dsviz'],
    install_requires=[],
)
