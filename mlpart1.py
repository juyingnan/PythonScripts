IN = open('cd6.pos')
words = ['NULL', 'NULL', 'NULL']
line = 'doobly-doo'

for x in range(0,2):
    line = IN.readline()
    wp = line.split()
    words.append(wp[0])

while line:
    line = IN.readline()
    wp = line.split()
    if len(wp):
        words.pop(0)
        words.append(wp[0])
        for word in words:
            print word + "\t",
        print ""
    else:
        for z in range (0,2):
            words.pop(0)
            words.append('NULL')
            for word in words:
                print word + "\t",
            print ""
        words = ['NULL', 'NULL', 'NULL']
        for x in range(0,2):
            line = IN.readline()
            if len(line) < 1:
                break
            wp = line.split()
            words.append(wp[0])

IN.close()
