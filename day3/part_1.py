#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def main():
    """ Main program """
    with open("day3/input.txt", "r") as f:
        input = f.read()
    lst = re.findall(r"mul\(\d+,\d+\)", input)
    result =[]
    for op in lst:
        op = re.split(r"\(|\)|,", op)
        if "mul" in op:
            result.append(int(op[1])*int(op[2]))
    print(sum(result))

if __name__ == "__main__":
    main()