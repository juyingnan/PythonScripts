#!/usr/bin/python

# Yue Chen



def mystery(ins, outs):
    if not ins:
        return outs
    else:
        if len(ins) > len(outs):
            return mystery(ins[1:], outs + ins[0])
        else:
            return mystery([], ins + outs)


def my_mystery(ins):
    # start = 0
    end = len(ins)
    mid = -(-end // 2) # easy ceil without math package
    return ins[mid:] + ins[0:mid]


word = raw_input('give me a capital of a European country: ')
print mystery(word, '')
print my_mystery(word)

print
print "Other Samples: "
input_list = ["Athens", "Paris", "Reykjavik", "Rome"]
for input in input_list:
    print mystery(input, '')
    print my_mystery(input)
