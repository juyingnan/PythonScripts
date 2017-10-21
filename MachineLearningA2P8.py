#!/usr/bin/env python3
# MachineLearningA2P8.py : About EM Algorithm
# Yingnan Ju & Yue Chen, Oct 2017

# This exercise will give you some practice coding the EM algorithm. We will apply the mixture of
# Gaussian technique to one-dimensional data . You will hand a data set on Canvas: data1(txt). Create
# a program to estimate the means, standard deviations, and weights of a mixture of Gaussian via the
# EM algorithm. You will probably want to have three functions: one that performs the expectation
# step, one that performs the maximization step, and one that runs the outer loop. Be sure to include
# all code and plots in your homework submission.


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


# main function
# solve the problem
# inputs are list and how many distributions in it
def solve(data_list, number_of_group):
    # get initial groups
    data_list.sort()
    grouped_list = get_divided_list(data_list, number_of_group)

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
        current_expectation_list = [get_expectation(group) for group in grouped_list]
        current_deviation_list = [get_deviation(group) for group in grouped_list]
    return grouped_list


# Test code
# file name is data1.txt
file_path = 'data1.txt'
# Get data
Initial_data_list = get_data(file_path)
# print(data)
# Calculate data
group_count = 3
solution = solve(Initial_data_list, group_count)
# print result
for distribution in solution:
    print("Set ", solution.index(distribution) + 1)
    print("\tExpectation: ", get_expectation(distribution))
    print("\tDeviation: ", get_deviation(distribution))
    print("\tWeight: ", 1.0 * len(distribution) / sum([len(s) for s in solution]))
