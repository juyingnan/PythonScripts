#!/bin/python

# Professor Sandra Kuebler
# Apply ML Techniques in CL
# Yue Chen, Hai Hu and Eriya Terada
# March 13th, 2016

# minidom
from xml.dom import minidom


# Define wordClass
class wordClass:
    def __init__(self, instanceId, senseId, context):
        self.instancdId = instanceId
        self.sensId = senseId
        self.context = context


# Open the files and read in the data
def openRead(fileName):
    xmlDoc = minidom.parse(fileName)

    instanceList = xmlDoc.getElementsByTagName('instance')
    # print(len(instanceList))
    # for instance in instanceList:
    #     print(instance.attributes['id'].value)

    answerList = xmlDoc.getElementsByTagName('answer')
    # print(len(answerList))
    # for answer in answerList:
    #     print(answer.attributes['senseid'].value)

    contextList = xmlDoc.getElementsByTagName('context')
    # print(len(contextList))
    # for context in contextList:
    #     print(context.firstChild.nodeValue)

    i = 0
    worldclasslist = []
    while i < len(instanceList):
        worldclasslist.append(
            wordClass(instanceList[i].attributes['id'].value, answerList[i].attributes['senseid'].value,
                      contextList[i].firstChild.nodeValue))
        i += 1

    return worldclasslist


# varibles in arguments and def should be different from varibles outside
# Extract context features
def extractContextFeature(wordclasslist):
    i = 0
    contextfeature = ""
    while i < len(wordclasslist):
        contextfeature += wordclasslist[i].context
        i += 1
    contextfeature = contextfeature.replace('\n', '')
    contextfeature = contextfeature.split(" ")
    contextfeature = list(set(contextfeature))
    contextfeature.remove('')
    return contextfeature


def createFeatureMatrix(contextfeature, wordclasslist):
    featurematrix = []
    for wordclass in wordclasslist:
        wordclasscontext = wordclass.context.replace('\n', '').split(' ')
        featureline = [0] * len(contextfeature)
        for i in range(0, len(featureline)):
            for word in wordclasscontext:
                if word == contextfeature[i]:
                    featureline[i] = 1
                    # break
        featurematrix.append(featureline)
    return featurematrix


# Main

# Open the files and read in the data
print 'please input the file name: '
fileName = raw_input(" ")
wordClassList = openRead(fileName)

# Extract context features
contextFeature = extractContextFeature(wordClassList)

import time
start_time = time.time()
# Create feature matrix
featureMatrix = createFeatureMatrix(contextFeature, wordClassList)
elapsed_time = time.time() - start_time
print elapsed_time

# write to file
fileWriter = open(fileName + "_matrix.txt", 'wb')
for featureline in featureMatrix:
    for bit in featureline:
        fileWriter.write(str(bit)+'\t')
    fileWriter.write('\n')
fileWriter.close()

# read file
fileReader = open(fileName + "_matrix.txt")
lines = fileReader.readlines()
listMatrix = []
for line in lines:
    linelist = line.strip().split('\t')
    listMatrix.append(linelist)
