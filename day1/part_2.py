#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def main():
    """ Main program """
    lst_1, lst_2 = [], []
    with open("day1/input.txt", "r") as f:
        for line in f:
            ln = line.replace("\n", "").split("   ")
            lst_1.append(int(ln[0]))
            lst_2.append(int(ln[1]))
    result_list = []
    for x in lst_1:
        result_list.append(x * lst_2.count(x))
    print(sum(result_list))
    

if __name__ == "__main__":
    main()