import cv2
import os

TRANSPARENT_RATIO_THRESHOLD = 0.5
FILE_SIZE_LOWER_THRESHOLD = 16000
FILE_SIZE_UPPER_THRESHOLD = 25000
SEPARATOR = '|'
FILTERED_FOLDER_NAME = 'filtered'
FOLDER_PATH = r'C:\Users\bunny\Desktop\images-227'
FILTER_PATH = 'temp.txt'


def calculate_transparent_ratio(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    total_count = 0.0
    trans_count = 0.0
    for row in img[::3]:
        for pixel in row[::3]:
            total_count += 1
            if len(pixel) > 3:
                if pixel[3] == 0:
                    trans_count += 1
            else:
                return 0.0
            # print(pixel[3], end=' ')
        # print()
    ratio = trans_count / total_count
    # print(ratio)
    return ratio


def get_image_transparent_ratio(root_path, output_file_path):
    fp = open(output_file_path, 'w')
    count = 0
    for root, dirs, files in os.walk(root_path):
        for file in files:
            count += 1
            path = os.path.join(root, file)
            transparent_ratio = calculate_transparent_ratio(path)
            fp.write(path + SEPARATOR + transparent_ratio.__str__() + '\n')
            # if count % 500 == 0:
            #     print(count)
            # print(calculate_transparent_ratio(path))
    fp.close()


def filter_image(filter_file_path):
    fp = open(filter_file_path, 'r')
    lines = fp.readlines()
    for line in lines:
        content = line.split(SEPARATOR)
        file_path = content[0]
        file_transparent_ratio = float(content[1])
        file_info = os.stat(file_path)
        file_size = file_info.st_size
        if (file_transparent_ratio > TRANSPARENT_RATIO_THRESHOLD and file_size < FILE_SIZE_UPPER_THRESHOLD) \
                or file_size < FILE_SIZE_LOWER_THRESHOLD:
            # move them to another folder
            file_path = content[0]
            directory = os.path.dirname(file_path)
            file_name = os.path.basename(file_path)
            new_directory = directory + '\\' + FILTERED_FOLDER_NAME + '\\'
            # print(new_directory)
            # print(new_directory + file_name)
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
            if os.path.exists(file_path):
                os.rename(file_path, new_directory + file_name)


get_image_transparent_ratio(FOLDER_PATH, FILTER_PATH)
filter_image(FILTER_PATH)
