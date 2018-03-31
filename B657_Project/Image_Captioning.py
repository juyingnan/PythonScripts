# %matplotlib inline
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from B657_Project.cache import cache

from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Input, Dense, GRU, Embedding
from tensorflow.python.keras.applications import VGG16
from tensorflow.python.keras.optimizers import RMSprop
from tensorflow.python.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

print("TensorFlow Version: " + tf.__version__)
print("Keras Version: " + tf.keras.__version__)
print()

from B657_Project import coco

coco.set_data_dir("d:/coco/")
_, filenames_train, captions_train = coco._load_records(train=True)
_, filenames_val, captions_val = coco._load_records(train=False)

num_images_train = len(filenames_train)
num_images_cal = len(filenames_val)
print("Number of images in the training-set: " + str(num_images_train))
print("Number of images in the validation-set: " + str(num_images_cal))
