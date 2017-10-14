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
    roll_operation = [True, False]
    possible_dice_result = [1, 2, 3, 4, 5, 6]
    solution = [False, False, False]
    max_result = sum_three_dice(d_list)
    for roll_1 in roll_operation:
        for roll_2 in roll_operation:
            for roll_3 in roll_operation:
                roll_decision_list = [roll_1, roll_2, roll_3]
                roll_possible_result_list = []
                possibility = 1.0
                for i in range(0, len(d_list)):
                    roll_possible_result_list.append(possible_dice_result if roll_decision_list[i] else [d_list[i]])
                    possibility /= len(roll_possible_result_list[i])
                possible_result = 0
                for d1 in roll_possible_result_list[0]:
                    for d2 in roll_possible_result_list[1]:
                        for d3 in roll_possible_result_list[2]:
                            possible_result += sum_three_dice([d1, d2, d3]) * possibility
                if possible_result > max_result:
                    max_result = possible_result
                    solution = roll_decision_list
    return solution, d_list, max_result


def sum_three_dice(d_list):
    return 25 if d_list[0] == d_list[1] and d_list[1] == d_list[2] else sum(d_list)


def print_solution(solution):
    for i in range(1, len(solution[0]) + 1):
        print("dice", i, ": ", solution[1][i - 1], ", ", "Roll." if solution[0][i - 1] is True else "Don't roll.")
    print("Current points: ", sum_three_dice(solution[1]))
    print("Expected points after decision: ", round(solution[2], 3))


# Get dice points from argv
dice_1 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
dice_2 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
dice_3 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
dice_list = [dice_1, dice_2, dice_3]

# get the solution and print
print_solution(solve(dice_list))
