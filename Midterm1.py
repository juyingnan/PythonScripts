#!/bin/python

# Yue Chen

import string

def function_a():
    aSentence = raw_input("Please input a sentence: ")
    vowel = 0
    consonant = 0
    vowel_list = 'aeiouAEIOU'
    consonant_list = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'

    for character in aSentence:
        if character in vowel_list:
            vowel += 1
        elif character in consonant_list:
            consonant += 1
    print "It has ", vowel, " vowel(s) and ", consonant, " consonant(s)."

def function_b():
    vowel = 0
    consonant = 0
    vowel_list = 'aeiouAEIOU'
    consonant_list = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    bSentence = raw_input("Please input a sentence: ")
    punctuation = string.punctuation
    bSentence = bSentence.translate(None, punctuation)
    words = bSentence.split(" ")
    for word in words:
        newWord = word
        vowel = 0
        consonant = 0
        for character in newWord:
            if character in vowel_list:
                vowel += 1
            elif character in consonant_list:
                consonant += 1
        print "It has ", vowel, " vowel(s) and ", consonant, " consonant(s) in word \"", newWord, "\""

def function_c():
    cSentence = raw_input("Please input a sentence: ")
    cLength = int(raw_input("What is the word length? "))
    punctuation = string.punctuation
    cSentence = cSentence.translate(None, punctuation)
    words = cSentence.split(" ")
    count = 0
    for word in words:
        if len(word) == cLength:
            count += 1
    print "There are ", count, " word(s) in this sentence that have ", cLength, " character(s)."

while (True):
    print
    print "This program has 3 functions:"
    print "\ta. Output the number of vowels and consonants in a sentence."
    print "\tb. Output the  number of vowels and consonants in each word of a sentence."
    print "\tc. Output the number of words of specific length in a sentence."
    option = raw_input("What do you want to do? (a, b, c) or Exit?(e)")
    if option == 'a':
        function_a()
    elif option == 'b':
        function_b()
    elif option == 'c':
        function_c()
    elif option == 'e':
        break
    else:
        print "Wrong input, please try again."
