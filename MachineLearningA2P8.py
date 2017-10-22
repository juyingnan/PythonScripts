#!/usr/bin/env python3
# MachineLearningA2P8.py : About EM Algorithm
# Yingnan Ju & Yue Chen, Oct 2017

# "This exercise will give you some practice coding the EM algorithm. We will apply the mixture of
# Gaussian technique to one-dimensional data . You will hand a data set on Canvas: data1(txt). Create
# a program to estimate the means, standard deviations, and weights of a mixture of Gaussian via the
# EM algorithm. You will probably want to have three functions: one that performs the expectation
# step, one that performs the maximization step, and one that runs the outer loop. Be sure to include
# all code and plots in your homework submission."

# instruction:
# just run this file
# data file path is data1.txt at line 112
# count of mixture of Gaussian is at line 115: group_count = 3
# change it to 2 or 4 for Question(b)

import math


# read data from file path into a list and return
def get_data(path):
    result = []
    with open(path) as f:
        read_data = f.readlines()
        for line in read_data:
            result.append(float(line))
    return result


# find the index of distribution group that a data should be put into
def get_max_index(data, expectation_list, deviation_list):
    distance_list = [1.0 * abs(data - expectation_list[i]) / deviation_list[i] for i in range(0, len(expectation_list))]
    return distance_list.index(min(distance_list))


# divide a list into num parts and each part is a list
# return the list of divided lists
def get_divided_list(long_list, num):
    avg = len(long_list) / float(num)
    result = []
    last = 0.0
    while last < len(long_list):
        result.append(long_list[int(last):int(last + avg)])
        last += avg
    return result


# get expectation from a data list
# if no data, expectation is 0
def get_expectation(data_list):
    return (1.0 * sum(data_list) / len(data_list)) if len(data_list) > 0 else 0


# get deviation from a data list
# if no data, deviation is .01
def get_deviation(data_list):
    expectation = get_expectation(data_list)
    d2 = (sum([(data - expectation) ** 2 for data in data_list]) / len(data_list)) if len(data_list) > 1 else 0.01
    return math.sqrt(d2)


def get_log_likelihood(grouped_data_list):
    flat_list = [data for group in grouped_data_list for data in group]
    total_likelihood = 0.0
    for data in flat_list:
        for group in grouped_data_list:
            likelihood = 1.0 * abs(data - get_expectation(group)) / get_deviation(group) \
                         * len(grouped_data_list) / len(flat_list)
            total_likelihood += (math.log(likelihood) if likelihood > 0 else 0)
    return total_likelihood


# main function
# solve the problem
# inputs are list and how many distributions in it
def solve(data_list, number_of_group):
    # get initial groups
    data_list.sort()
    grouped_list = get_divided_list(data_list, number_of_group)
    log_likelihood_list = []

    # get expectation list that to be compared
    current_expectation_list = [get_expectation(group) for group in grouped_list]
    # current_deviation_list = [get_deviation(group) for group in grouped_list]
    current_deviation_list = [1000.0] * len(grouped_list)
    last_expectation_list = [0.0] * len(grouped_list)

    # compare current groups with last one
    # threshold: 0.001
    threshold = 0.001
    while max([abs(current_expectation_list[i] - last_expectation_list[i])
               for i in range(0, number_of_group)]) > threshold:
        last_expectation_list = list(current_expectation_list)
        temp_list = []
        for i in range(number_of_group):
            temp_list.append([])

        for data in data_list:
            temp_list[get_max_index(data, current_expectation_list, current_deviation_list)].append(data)

        # refresh group data
        grouped_list = temp_list
        log_likelihood_list.append(get_log_likelihood(grouped_list))
        current_expectation_list = [get_expectation(group) for group in grouped_list]
        current_deviation_list = [get_deviation(group) for group in grouped_list]
    return grouped_list, log_likelihood_list


# Test code
# file name is data1.txt
file_path = 'data1.txt'
# Get data
initial_data_list = get_data(file_path)
# print(data)
# Calculate data
# change this group count to 2 or 4 for question(b)
group_count = 3
solution = solve(initial_data_list, group_count)
# print result
for distribution in solution[0]:
    print("Set ", solution[0].index(distribution) + 1)
    print("\tExpectation: ", get_expectation(distribution))
    print("\tDeviation: ", get_deviation(distribution))
    print("\tWeight: ", 1.0 * len(distribution) / sum([len(s) for s in solution[0]]))

# Python plot
# this part is to plot graph
# uncomment this part to plot
# import numpy
# import matplotlib.pyplot as plt
#
# color_list = ["r-", "g-", "b-", "y-"]
# color_index = 0
# for distribution in solution[0]:
#     u = get_expectation(distribution)  # μ
#     sig = get_deviation(distribution)  # 差δ
#     x = numpy.linspace(u - 3 * sig, u + 3 * sig, 50)
#     y_sig = numpy.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
#     # plt.plot(x, y_sig, color_list[color_index % len(color_list)], linewidth=2)
#     color_index += 1
#     plt.grid(True)
# x = numpy.linspace(0, 5, 50)
# y = solution[1]
# plt.plot(range(len(y)), y, "b-", linewidth=2)
# plt.grid(True)
# plt.show()
