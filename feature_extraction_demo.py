import string
import csv
import pickle
import re


# first, define a class for each line
class tweet_line:
    # initial
    def __init__(self, id, target, tweet, stance):
        self.id = id
        self.target = target
        self.tweet = tweet
        self.stance = stance
        self.statistics = {}
        self.collect_statistics()
        self.isIntegrated = False
        self.check_integrity()

    # check if all variables are string
    def check_integrity(self):
        self.isIntegrated = True
        if not isinstance(self.id, str):
            self.isIntegrated = False
        if not isinstance(self.target, str):
            self.isIntegrated = False
        if not isinstance(self.tweet, str):
            self.isIntegrated = False
        if not isinstance(self.stance, str):
            self.isIntegrated = False

    # set tweet content and auto collect statistics
    def set_tweet_content(self, tweet):
        self.tweet = tweet
        self.collect_statistics()

    # calculate frequency of each word in tweet field
    def collect_statistics(self):
        # statistics clear
        self.statistics.clear()
        # remove all punctuations
        # TODO 1: how to handle '#' and '@' ???
        # # and @ will be kept with the word, e.g. #SemST will be treated as one word.
        clean_tweet = self.remove_punctuation_from_string(self.tweet)
        # get word list
        words = clean_tweet.split(" ")
        for word in words:
            if self.statistics.has_key(word):
                self.statistics[word] += 1
            else:
                self.statistics[word] = 1

    def remove_punctuation_from_string(self, string_):
        # step 1: trans all punctuations(except '#' and '@') to "punctuation between spaces"
        # punctuations should be kept as separate words.
        punctuation = string.punctuation
        punctuation = punctuation.replace('#', '')
        punctuation = punctuation.replace('@', '')
        for char in string_:
            if char in punctuation:
                string_ = string_.replace(char, ' ' + char + ' ')
        # trans_table = string.maketrans(punctuation, ' ' * len(punctuation))
        # clean_tweet = string_.translate(trans_table)
        # step 2: remove more spaces
        clean_tweet = ' '.join(string_.split())
        return clean_tweet

    # define output/print format
    def __str__(self):
        separator = "||"
        return self.id + separator + self.target + separator + self.tweet + separator + self.stance + separator + str(
            self.statistics)


def read_tweet_file(path, separator="\t"):
    result = []
    # get all data, each row is a dict
    reader = csv.DictReader(open(path), delimiter='\t')
    for row in reader:
        temp_tweet_line = tweet_line(id=row["ID"],
                                     target=row["Target"],
                                     tweet=row["Tweet"],
                                     stance=row["Stance"])
        # TODO 2: if not integrated, append or not?
        if temp_tweet_line.isIntegrated is True:
            result.append(temp_tweet_line)
        else:
            print "Error Line: ", row
    return result


def tweet_filter(tweet_list, id=None, target=None, tweet=None, stance=None):
    result = []
    # arg1 is list or tuple or not
    if not isinstance(tweet_list, (list, tuple)):
        return result
    else:
        for temp_tweet_line in tweet_list:
            if id is not None:
                # id : exact
                if id.lower() != temp_tweet_line.id.lower():
                    continue
            if target is not None:
                # target : contain
                if target.lower() not in temp_tweet_line.target.lower():
                    continue
            if tweet is not None:
                # tweet : contain
                if tweet.lower() not in temp_tweet_line.tweet.lower():
                    continue
            if stance is not None:
                # stance : exact
                if stance.lower() != temp_tweet_line.stance.lower():
                    continue
            result.append(temp_tweet_line)
    return result


# process starts
# pre define separator and file path
separator = "\t"
file_path = "semeval2016-task6-trainingdata.txt"
# get all tweets
all_tweet_list = read_tweet_file(file_path, separator)  # arg separator can be ignored

# pickle save
pickle.dump(all_tweet_list, open("feature_extraction_temp.txt", "w"))
# pickle read
another_list = pickle.load(open("feature_extraction_temp.txt", "r"))

# print some results: count, first and last line
print "Count of all: ", len(another_list)
print another_list[0]
print "..."
print another_list[-1]
print

# filter test
filter_1 = "hillary"
filter_2 = "AGAINST"
list_with_hillary = tweet_filter(another_list, target=filter_1)
list_with_hillary_and_against = tweet_filter(another_list, target=filter_1, stance=filter_2)
print "Count of filter_1 (hillary) result: ", len(list_with_hillary)
print list_with_hillary[0]
print "..."
print list_with_hillary[-1]
print
print "Count of filter_2 (hillary+AGAINST) result: ", len(list_with_hillary_and_against)
print list_with_hillary_and_against[0]
print "..."
print list_with_hillary_and_against[-1]
