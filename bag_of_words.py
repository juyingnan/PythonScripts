import string


# get a punctuation translator to remove punctuation,
# parameter is a string that includes all punctuation that you don't want to remove
# e.g. if you don't want to remove '#' and '@' from a tweet, just use '@#' as the parameter
def get_translator(exclude_chars=''):
    exclude = string.punctuation
    for char in exclude_chars:
        exclude = exclude.replace(char, '')
    return str.maketrans('', '', exclude)


# get full word list from a line of tweet
# parameter without_at_and_sharp is a bool,
#   True: remove all words starting with '@' and '#'
#   False: keep all words starting with '@' and '#'
def get_full_word_from_line(line, without_at_and_sharp):
    filtered_line = line.translate(translator)
    full_words = filtered_line.split()
    filtered_words = [_word for _word in full_words if not _word.startswith('http')]
    if without_at_and_sharp:
        filtered_words = [_word for _word in filtered_words if not (_word.startswith('@') or _word.startswith('#'))]
    filtered_words = [_word for _word in filtered_words if len(_word) > 0]
    return filtered_words


is_remove_at_and_sharp = True
translator = get_translator('@#')

train_file_path = r'C:\Users\bunny\Desktop\test.txt'
test_file_path = r'C:\Users\bunny\Desktop\test2.txt'

# get content from train and test file and combine them in a full_lines
train_lines = open(train_file_path, 'r')
test_lines = open(test_file_path, 'r')
train_lines = [line for line in train_lines]
test_lines = [line for line in test_lines]
full_lines = train_lines + test_lines

# get a full word list that includes all word from train and test tweets
full_word_list = []
for line in full_lines:
    words = get_full_word_from_line(line, is_remove_at_and_sharp)
    for word in words:
        if word not in full_word_list:
            full_word_list.append(word)
#     print(words)
# print(full_word_list)
total_words_number = len(full_word_list)

# get a full matrix
full_matrix = []
for line in full_lines:
    full_matrix.append([0] * total_words_number)
    words = get_full_word_from_line(line, is_remove_at_and_sharp)
    for word in words:
        index = full_word_list.index(word)
        full_matrix[-1][index] = 1
# for line in full_matrix:
#     print(line)

# get train and test matrix
train_matrix = full_matrix[:len(train_lines)]
test_matrix = full_matrix[len(train_lines):]
