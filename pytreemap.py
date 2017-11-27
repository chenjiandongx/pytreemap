#!/usr/bin/env python
# coding=utf-8

import argparse

from jinja2 import Environment
from template import TEMPLATE

TPL = Environment().from_string(TEMPLATE)

VERSION = "VERSION 0.0.1"


def get_parser():
    """ 解析命令行参数
    """
    parser = argparse.ArgumentParser(description='TreeMap-Generator CLI Tools.')
    parser.add_argument('-o', '--output', type=str,
                        help='output html file path')
    parser.add_argument('-i', '--input', type=str,
                        help='input json data path')
    parser.add_argument('-d', '--direction', type=str,
                        help='direction of TreeMap, '
                             'it can be LR/RL/H/TB/BT/V.(default LR)')
    parser.add_argument('-v', '--version', action='store_true',
                        help='version information.')
    return parser


def command_line_runner():
    """ 执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(VERSION)
        return

    if not args['input']:
        parser.print_help()
    else:
        render(
            path=args["output"] or "TreeMap.html",
            direction=args["direction"] or "LR",
            data=get_data(args['input'])
        )


def get_data(path):
    """ 读取数据

    :param path: 数据路径
    """
    data = ""
    try:
        with open(path, "r", encoding="utf8") as fread:
            data = fread.read()
    except FileNotFoundError:
        print("File Not Found!")
    return data


def render(path, direction, data=None):
    """ 渲染模板生成网页

    :param path: 文件保存路径，默认为 'TreeMap.html'
    :param direction: 树图方向，有（LR/RL/H/TB/BT/V）可选，默认为 'LR'
    :param data: json 数据
    """
    try:
        with open(path, "w+", encoding="utf-8") as fout:
            fout.write(
                TPL.render(direction=direction, json_data=data))
    except OSError:
        print("Invalid file path!")


if __name__ == "__main__":
    command_line_runner()
