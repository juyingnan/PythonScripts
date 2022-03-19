#!/usr/bin/python

# Yue Chen

# Reading the file

def readFile(filePath):
    file = open(filePath,'r')
    line = "XXX"
    lineSplit = []
    pos = []
    while line:
        line = file.readline()
        if line.__len__() > 1:
            lineSplit = line.split()
            pos.append(lineSplit)
    return pos

# Creating the ambuguity classes

def ambiguityClass(pos):
    ambiguition = {}
    for word in pos:
        if ambiguition.has_key(word[0]):
            plist = ambiguition[word[0]]
            if word[1] not in plist:
                plist.append(word[1])
                ambiguition[word[0]] = plist
        else:
            ambiguition[word[0]] = [word[1]]
    return ambiguition

# Providing the user with the ambiguity class for a word that the user inputs

def printAmbiguityClass(ambiguition):
    inputWord = raw_input("Please enter a word: ")
    print inputWord
    print ambiguition[inputWord]
    return 0

# Providing a list of all words that have a given number of POS tags

def printWords(ambiguition):
    inputNumber = int(raw_input("Please enter a number: "))
    for (word,pos) in ambiguition.items():
        if len(pos) == inputNumber:
            print word
    return 0

# Main

filePath = "cd6.pos"

pos = readFile(filePath)

ambiguition = ambiguityClass(pos)

print "This program has two functions."
print "(a) It provides the user with the ambiguity class for a word that the user inputs."
print "(b) It provides a list of all words that have a given number of POS tags."

option = raw_input("Please choose one option to begin: (a/b) ")

if option == "a":
    printAmbiguityClass(ambiguition)
elif option == "b":
    printWords(ambiguition)