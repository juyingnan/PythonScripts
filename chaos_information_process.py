import csv
import pickle
import os


# this function is to find out the enlarged range
def get_range(int_list):
    min_id = min(int_list)
    max_id = max(int_list)
    return [min_id, max_id]


# to process each group of lines
def process_group(words_group):
    result = []
    combinations = []

    # 1st round, found all "MWE" and make combinations
    for line in words_group:
        id = line[1]
        context = line[3]
        if line[4] == "MWE":
            line_added = False
            # if combination exists, enlarge the range
            for item in combinations:
                min = item[0]
                max = item[1]
                if (context >= min and context <= max) or (id >= min and id <= max):
                    new_item = get_range([min, max, id, context])
                    combinations.remove(item)
                    combinations.append(new_item)
                    line_added = True
            # if combination doesn't exist, create one
            if line_added is False:
                id_range = get_range([context, id])
                combinations.append(id_range)

    # 2nd round, add missing lines into combinations and enlarge the range
    # the process of enlarging should be repeated until the result is constant
    if len(combinations) > 0:
        while True:
            last_combinations = []
            last_combinations.extend(combinations)
            for line in words_group:
                id = line[1]
                context = line[3]
                for item in combinations:
                    min = item[0]
                    max = item[1]
                    if context >= min and context <= max:
                        new_item = get_range([min, max, id, context])
                        combinations.remove(item)
                        combinations.append(new_item)
            is_changed = False
            for i in range(0, len(combinations)):
                if last_combinations[i][0] != combinations[i][0] or last_combinations[i][1] != combinations[i][1]:
                    is_changed = True
                    break
            if not is_changed:
                break
                # following two lines can print which lines need repeating process
                # else:
                #     print words_group[0][0]

    # return results
    # added_line_list = []
    for item in combinations:
        min = item[0]
        max = item[1]
        # delete those combinations longer than 5 words
        if (max - min < 5):
            has_v_tag = False
            for i in range(min - 1, max):
                if words_group[i][5] == "V":
                    has_v_tag = True
                    # print words_group[i][0], words_group[i][2]
            # delete those combinations that have V tag
            if not has_v_tag:
                # result_string = str(words_group[min - 1][0]) + ": "  # print line number for readability
                result_string = ""
                for i in range(min - 1, max):
                    result_string += words_group[i][2] + " "
                    # added_line_list.append(i+1)
                # print result_string
                result.append(result_string)

    # add items with "^" tag
    # for line in words_group:
    #     id = line[1]
    #     tag = line[5]
    #     word = line[2]
    #     if tag == "^" and id not in added_line_list:
    #         # print line
    #         result.append(word)

    return result


def read_chaos_file(path, separator="\t"):
    wordw_group_result = []
    words_group = []
    proper_noun_result = []
    # get all data, each row is a dict
    reader = csv.reader(open(path), delimiter='\t')
    line_number = 0
    for row in reader:
        line_number += 1
        if len(row) > 0:
            id = int(row[0])
            word = row[1]
            # print line_number, row[1]
            tag = row[3]
            context = int(row[6])
            type = row[7]
            words_group.append([line_number, id, word, context, type, tag])
            # get proper noun
            if tag == "^":
                proper_noun_result.append(word)
        else:
            # it means the end of one group
            group_result = process_group(words_group)
            if group_result is not None:
                wordw_group_result.extend(group_result)
            words_group = []
    return wordw_group_result, proper_noun_result


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
    for info in list:
        # fight with single quote
        info = info.replace("\\\'", "\'").replace('\\\"', '\"')
        result.append(info)
    return result


def post_process(l):
    unique_info = unique(l)
    sorted = sort(unique_info)
    return sorted
    # all_info_list = sorted(set(all_info_list)) # Work for list?
    # if 5 spaces in member, delete it
    # if label has V, delete it


def unique(l):
    result = set(l)
    result = list(result)
    return result


def sort(l):
    result = sorted(l)
    return result


def delete_file(filepath):
    os.remove(filepath)


# process starts
separator = "\t"
file_path = "semeval2016-task6-trainingdata_sents_utf8.predict"

# fight with single quote
new_file_path = process_quote_in_file(file_path)
# get results
all_info_list, proper_noun_list = read_chaos_file(new_file_path, separator)
delete_file(new_file_path)

print "Count of all groups: ", len(all_info_list)
all_info_list = process_quote_in_list(all_info_list)
all_info_list = post_process(all_info_list)
for line in all_info_list:
    print line

print
print "Count of all proper noun: ", len(proper_noun_list)
proper_noun_list = process_quote_in_list(proper_noun_list)
proper_noun_list = post_process(proper_noun_list)
for line in proper_noun_list:
    print line

# pickle save
pickle.dump(all_info_list, open("feature_extraction_groups_temp.txt", "w"))
pickle.dump(proper_noun_list, open("feature_extraction_proper_noun_temp.txt", "w"))
