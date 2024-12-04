#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def main():
    """ Main program """
    lst = []
    differences = []
    report = []
    with open("day2/input.txt", "r") as f:
        for line in f:
            lst.append((line.replace("\n", "").split(" ")))
    for numbers in lst:
        differences = ([int(numbers[i]) - int(numbers[i + 1]) for i in range(len(numbers) - 1)])
        if all(x != 0 and abs(x) <= 3 for x in differences) and all((x > 0) == (differences[0] > 0) for x in differences):
            report.append(True)
    print(len(report))


if __name__ == "__main__":
    main()