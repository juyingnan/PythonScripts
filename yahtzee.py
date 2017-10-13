#!/usr/bin/env python3
# yahtzee.py : Solve the best solution of Yahtzee game
# Yingnan Ju, Oct 2017
#
# Three dice given, find a best strategy for next step
# d1 = d2 = d3: 25 points
# else, d1 + d2 + d3 points

import sys


# main function to solve the problem
def solve(d_list):
    for dice in d_list:
        if dice <= 0:
            return "Wrong dice. Are you cheating?"


# Get dice points from argv
dice_1 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
dice_2 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
dice_3 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
dice_list = [dice_1, dice_2, dice_3]

# get the solution and print
solution = solve(dice_list)
print(solution)
