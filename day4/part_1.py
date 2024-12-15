#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def main():
    """ Main program """
    game_field = []
    with open("day4/input.txt", "r") as f:
        for line in f:    
            game_field.append(line.replace("\n", ""))
    xmas_string = game_field
    xmas_string_reversed = game_field[::-1]
    xmas_string_diag = [tup[0] for tup in list(zip(game_field))]
    xmas_string_diag_reserved = [tup[0] for tup in list(zip(xmas_string_reversed))]
    xmas_string_joined = xmas_string + xmas_string_reversed + xmas_string_diag + xmas_string_diag_reserved
    xmas_string_found = re.findall("XMAS", ' '.join(xmas_string_joined))
    print(len(xmas_string_found))

if __name__ == "__main__":
    main()