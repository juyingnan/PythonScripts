IN = open('cd6.pos')
ambi = {}

for line in IN:
    # get rid of the linebreak at the end of the file
    line = line.strip()
    if line:
        #instead of extracting a list, I'm extracting a tuple, and then have two individual variables; I can do that because I know, there are only two entries in the line
        (word, pos) = line.split('\t')
        if ambi.has_key(word):
            plist = ambi[word]
            if pos not in plist:
                plist.append(pos)
                ambi[word] = plist
        else:
            ambi[word] = [pos]
IN.close()

print ambi
