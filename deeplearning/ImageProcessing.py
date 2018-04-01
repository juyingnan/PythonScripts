from skimage import io
from skimage.transform import resize
from skimage.color import rgb2hed
from skimage.exposure import rescale_intensity
import glob
import os
import numpy as np

# 数据集地址
image_path = 'c:/Users/bunny/Desktop/dataset1_hed/root/'

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
            img = io.imread(im)
            img = resize(img, (new_width, new_height))
            io.imsave(im, img)
            del img
            count += 1
            if count % 2500 == 0:
                print(count)


def stain_separate_image(root_path):
    cate = [root_path + folder for folder in os.listdir(root_path) if os.path.isdir(root_path + folder)]
    count = 0
    for idx, folder in enumerate(cate):
        print('reading the images:%s' % folder)
        for im in glob.glob(folder + '/*.jpg'):
            img = io.imread(im)
            ihc_hed = rgb2hed(img)
            # Rescale hematoxylin and DAB signals and give them a fluorescence look
            _h = rescale_intensity(ihc_hed[:, :, 0], out_range=(0, 1))
            _d = rescale_intensity(ihc_hed[:, :, 2], out_range=(0, 1))
            zdh = np.dstack((np.zeros_like(_h), _d, _h))
            io.imsave(im, zdh)
            del img
            count += 1
            if count % 1000 == 0:
                print(count)


# resize_img(image_path, w, h)
stain_separate_image(image_path)
