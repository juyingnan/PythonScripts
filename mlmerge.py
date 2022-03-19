def get_all_possible_tags(file_path):
    IN = open(file_path)
    ambi = {}

    for line in IN:
        # get rid of the linebreak at the end of the file
        line = line.strip()
        if line:
            # instead of extracting a list, I'm extracting a tuple, and then have two individual variables; I can do that because I know, there are only two entries in the line
            (word, pos) = line.split('\t')
            if ambi.has_key(word):
                plist = ambi[word]
                if pos not in plist:
                    plist.append(pos)
                    ambi[word] = plist
            else:
                ambi[word] = [pos]

    IN.close()
    # print ambi
    return ambi


def list_to_string(l):
    string = ""
    for item in l:
        string += item + "_"
    string = string[0:-1]
    return string


def get_words(filepath):
    IN = open(filepath)
    words = ['NULL', 'NULL', 'NULL']
    tags = ['NULL', 'NULL', 'NULL']
    ambi_tags = [['NULL'], ['NULL'], ['NULL']]
    line = 'doobly-doo'
    ambi_dict = get_all_possible_tags(filepath)

    print "w-2\tw-1\tw\tw+1\tw+2\tp-2\tp-1\tac\tac+1\tac+2"
    for x in range(0, 2):
        line = IN.readline()
        wp = line.split()
        words.append(wp[0])
        tags.append(wp[1])
        ambi_tags.append(ambi_dict[wp[0]])

    while line:
        line = IN.readline()
        wp = line.split()
        if len(wp):
            words.pop(0)
            words.append(wp[0])
            tags.pop(0)
            tags.append(wp[1])
            ambi_tags.pop(0)
            ambi_tags.append(ambi_dict[wp[0]])
            for word in words:
                print word + "\t",
            for i in range(0, 2):
                print tags[i] + "\t",
            for i in range(2, 5):
                print list_to_string(ambi_tags[i]) + "\t",
            print ""
        else:
            for z in range(0, 2):
                words.pop(0)
                words.append('NULL')
                tags.pop(0)
                tags.append('NULL')
                ambi_tags.pop(0)
                ambi_tags.append(['NULL'])
                for word in words:
                    print word + "\t",
                for i in range(0, 2):
                    print tags[i] + "\t",
                for i in range(2, 5):
                    print list_to_string(ambi_tags[i]) + "\t",
                print ""
            words = ['NULL', 'NULL', 'NULL']
            tags = ['NULL', 'NULL', 'NULL']
            ambi_tags = [['NULL'], ['NULL'], ['NULL']]
            for x in range(0, 2):
                line = IN.readline()
                if len(line) < 1:
                    break
                wp = line.split()
                words.append(wp[0])
                tags.append(wp[1])
                ambi_tags.append(ambi_dict[wp[0]])
    IN.close()


filepath = 'cd6.pos'
get_words(filepath)
