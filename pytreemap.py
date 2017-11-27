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
    parser.add_argument('-i', '--input', type=str,
                        help='input json data path')
    parser.add_argument('-o', '--output', type=str, default="TreeMap.html",
                        help='output html file path')
    parser.add_argument('-d', '--direction', type=str, default="LR",
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
            input=args['input'],
            output=args["output"],
            direction=args["direction"],
        )


def render(input, direction="LR", output="TreeMap.html"):
    """ 渲染数据生成网页

    :param input: 输入 json 文件路径
    :param direction: 树图方向，有 LR/RL/H/TB/BT/V 可选
    :param output: 输出 html 文件路径
    """
    json_data = ""
    try:
        with open(input, "r", encoding="utf8") as fread:
            json_data = fread.read()
    except FileNotFoundError:
        print("File Not Found!")

    try:
        with open(output, "w+", encoding="utf-8") as fout:
            fout.write(
                TPL.render(direction=direction, json_data=json_data))
    except OSError:
        print("Invalid file path!")


if __name__ == "__main__":
    command_line_runner()
