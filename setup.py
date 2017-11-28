#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    name='pytm-cli',
    version="0.0.1",
    description="树图渲染命令行工具-利用 JSON 数据生成 HTML 格式的树图",
    url='https://github.com/chenjiandongx/pytm-cli',
    author_email='chenjiandongx@qq.com',
    license='MIT',
    py_modules=['pytreemap','template'],
    install_requires=['jinja2'],
    entry_points={
        'console_scripts':['pytm-cli=pytreemap:command_line_runner']
    }
)
