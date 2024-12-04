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
    lst_1 = np.sort(lst_1)
    lst_2 = np.sort(lst_2)
    print(lst_1)
    result_list = []
    for x, y in zip(lst_1, lst_2):
        result_list.append(abs(y - x))
    print(sum(result_list))
    

if __name__ == "__main__":
    main()