#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    name='pytm-cli',
    version="0.0.1",
    description="TreeMap-Generator CLI Tools",
    url='https://github.com/chenjiandongx/pytm-cli',
    author_email='chenjiandongx@qq.com',
    license='MIT',
    py_modules=['pytreemap','template'],
    install_requires=['jinja2'],
    entry_points={
        'console_scripts':['pytm-cli=pytreemap:command_line_runner']
    }
)
