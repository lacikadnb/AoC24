#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def main():
    """ Main program """
    with open("day3/input.txt", "r") as f:
        input = f.read()
    lst = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", input)
    filtered_lst = []
    skip = False
    for item in lst:
        if item == "don't()":
            skip = True
        elif item == "do()":
            skip = False
            continue  # Preskočiť "do()"
        if not skip:
            filtered_lst.append(item)    
    result =[]
    for op in filtered_lst:
        op = re.split(r"\(|\)|,", op)
        if "mul" in op:
            result.append(int(op[1])*int(op[2]))
    print(sum(result))

if __name__ == "__main__":
    main()