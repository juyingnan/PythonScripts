#!/bin/python

# Yue Chen

num = 1 # Error 1: "num = 0" => "num = 1", or the first while loop will not be executed.
numlist = []

while num != 0:
    num = int(raw_input('next num: '))
    numlist.append(num)
numlist.pop() # Error 2: pop 0, because 0 should not be in the list.
numlist.sort()

newnum = int(raw_input('new num: ')) # Error 3: int(), or newnum will be treated as a string.
done = 0
cnt = 0
while not done and cnt < len(numlist): # Error 4: add ":".
    if newnum < numlist[cnt]:
        numlist.insert(cnt, newnum)
        done = 1
    cnt+=1 # Error 5: cnt += 1, or infinite loop.
if not done:
    numlist.append(newnum)

print numlist 
