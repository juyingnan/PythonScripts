import cv2
import os

TRANSPARENT_RATIO_THRESHOLD = 0.5


def calculate_transparent_ratio(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    total_count = 0.0
    trans_count = 0.0
    for row in img:
        for pixel in row:
            total_count += 1
            if pixel[3] == 0:
                trans_count += 1
            # print(pixel[3], end=' ')
        # print()
    ratio = trans_count / total_count
    # print(ratio)
    return ratio


print(calculate_transparent_ratio('test.png'))

fp = open('temp.txt', 'w')
for root, dirs, files in os.walk(r'C:\Users\bunny\Desktop\images-227'):
    for file in files:
        path = os.path.join(root, file)
        transparent_ratio = calculate_transparent_ratio(path)
        fp.write(path + '|' + transparent_ratio.__str__() + '\n')
        # print(calculate_transparent_ratio(path))
fp.close()
