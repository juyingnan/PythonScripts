#!/usr/bin/env python3
# MachineLearningA2P8.py : About EM Algorithm
# Yingnan Ju & Yue Chen, Oct 2017

# This exercise will give you some practice coding the EM algorithm. We will apply the mixture of
# Gaussian technique to one-dimensional data . You will nd a data set on Canvas: data1(txt). Create
# a program to estimate the means, standard deviations, and weights of a mixture of Gaussian via the
# EM algorithm. You will probably want to have three functions: one that performs the expectation
# step, one that performs the maximization step, and one that runs the outer loop. Be sure to include
# all code and plots in your homework submission.

import sys


def get_data(path):
    result = []
    with open(path) as f:
        read_data = f.readlines()
        for line in read_data:
            result.append(float(line))
    return result


# file name is data1.txt
file_path = 'data1.txt'
data = get_data(file_path)
print(data)
