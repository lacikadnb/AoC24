#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def is_safe_report(differences):
    """
    Determines if a report is safe based on its differences.
    A report is safe if:
    - All differences are non-zero and within [-3, 3].
    - All differences have the same sign (all positive or all negative).
    """
    return all(x != 0 and abs(x) <= 3 for x in differences) and \
           all((x > 0) == (differences[0] > 0) for x in differences)

def main():
    """ Main program """
    lst = []
    safe_reports = 0
    
    # Read and process the input file
    with open("day2/input.txt", "r") as f:
        for line in f:
            lst.append(list(map(int, line.strip().split())))

    for numbers in lst:
        # Calculate differences
        differences = [numbers[i] - numbers[i + 1] for i in range(len(numbers) - 1)]
        
        # Check if the report is safe
        if is_safe_report(differences):
            safe_reports += 1
        else:
            # Try removing each level and recheck
            for i in range(len(numbers)):
                modified_numbers = numbers[:i] + numbers[i + 1:]
                modified_differences = [modified_numbers[j] - modified_numbers[j + 1] for j in range(len(modified_numbers) - 1)]
                if is_safe_report(modified_differences):
                    safe_reports += 1
                    break

    print(safe_reports)

if __name__ == "__main__":
    main()
