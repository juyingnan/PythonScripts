import csv
import os


# to process each group of lines
def process_group(words_group):
    result = []
    # id, word, head, label, tag
    for line in words_group:
        id = line[0]
        word = line[1]
        head = line[2]
        label = line[3]
        line_result = word + ": " + label
        while head != 0:
            next_line = words_group[head - 1]
            word = next_line[1]
            head = next_line[2]
            label = next_line[3]
            line_result += ", " + word + ", " + label
        line_result += ", 0"
        result.append(line_result)
    return result


def read_file(path, separator="\t"):
    result = []
    words_group = []
    # get all data, each row is a dict
    reader = csv.reader(open(path), delimiter='\t')
    line_number_start = 1
    line_number_end = 0
    sentence_number = 0
    for row in reader:
        line_number_end += 1
        if len(row) > 0:
            id = int(row[0])
            word = row[1]
            head = int(row[6])
            label = row[7]
            words_group.append([id, word, head, label])
        else:
            # it means the end of one group
            group_result = process_group(words_group)
            if group_result is not None:
                sentence_number += 1
                group_result.insert(0,
                                    "%% Sentence " + str(sentence_number) + " (line " + str(line_number_start) + "-" + str(
                                        line_number_end) + ")" + ": ")
                result.extend(group_result)
            words_group = []
            line_number_start = line_number_end + 1
    return result


def process_quote_in_file(file_path):
    new_file_path = file_path + "_"
    lines = open(file_path).readlines()
    fp = open(new_file_path, 'w')
    for s in lines:
        fp.write(s.replace('\"', '\\\"').replace("\'", "\\\'"))
    fp.close()
    return new_file_path


def process_quote_in_list(list):
    result = []
    for info in all_info_list:
        # fight with single quote
        info = info.replace("\\\'", "\'").replace('\\\"', '\"')
        result.append(info)
    return result


def delete_file(filepath):
    os.remove(filepath)


# process starts
separator = "\t"
file_path = "dep.txt"

# fight with single quote
new_file_path = process_quote_in_file(file_path)
all_info_list = read_file(new_file_path, separator)
all_info_list = process_quote_in_list(all_info_list)
delete_file(new_file_path)
for info in all_info_list:
    print info
