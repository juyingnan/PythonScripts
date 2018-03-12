import cv2
import glob
import os
import numpy as np

# 数据集地址
image_path = 'c:/Users/bunny/Desktop/dataset1/tmp/'
# 模型保存地址
model_path = 'c:/Users/bunny/Desktop/dataset1/root/model.ckpt'

# 将所有的图片resize成100*100
w = 100
h = 100
c = 3


# 读取图片
def resize_img(root_path, new_width, new_height):
    cate = [root_path + folder for folder in os.listdir(root_path) if os.path.isdir(root_path + folder)]
    count = 0
    for idx, folder in enumerate(cate):
        print('reading the images:%s' % folder)
        for im in glob.glob(folder + '/*.jpg'):
            img = cv2.imread(im)
            img = cv2.resize(img, (new_width, new_height))
            cv2.imwrite(im, img)
            del img
            count += 1
            if count % 2500 == 0:
                print(count)

resize_img(image_path, w, h)
