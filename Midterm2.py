#!/bin/python

# Yue Chen

import fileinput

fileName = raw_input("Please input the file name: ")

tags = []
counts = []

for line in fileinput.input(fileName):
    words = line.split("\t")
    if len(words) > 1:
        if words[1] not in tags:
        	words[1] = words[1].strip()
        	tags.append(words[1])
        	counts.append(0)
        counts[tags.index(words[1])] += 1

i = 0

while i < len(tags):
	print tags[i], counts[i]
	i += 1
