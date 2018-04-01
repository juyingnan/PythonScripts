from skimage import io
import glob
import os
import tensorflow as tf
import numpy as np
import time

# 数据集地址
image_path = 'c:/Users/bunny/Desktop/dataset1/root/'
# 模型保存地址
model_path = 'c:/Users/bunny/Desktop/dataset1/root/model.ckpt'

# 将所有的图片resize成100*100
w = 100
h = 100
c = 3
image_count = 10000
category_count = 3
learning_rate = 0.0001
regularization_rate = 0.00001
# 训练和测试数据，可将n_epoch设置更大一些
n_epoch = 100
current_batch_size = 64


# 读取图片
def read_img(path, total_count, size_filter=1500):
    cate = [path + folder for folder in os.listdir(path) if os.path.isdir(path + folder)]
    imgs = []
    labels = []
    for idx, folder in enumerate(cate):
        print('reading the images:%s' % folder)
        count = 0
        for im in glob.glob(folder + '/*.jpg'):
            # print('reading the images:%s'%(im))
            file_info = os.stat(im)
            file_size = file_info.st_size
            if file_size < size_filter:
                continue
            if file_size > 100 * size_filter:
                # print(im)
                continue
            img = io.imread(im)
            if img.shape != (w,h,3):
                print(im)
                continue
            imgs.append(img)
            labels.append(idx)
            count += 1
            if count > total_count:
                break
    return np.asarray(imgs, np.float32), np.asarray(labels, np.int32)


# -----------------构建网络 - ---------------------
# noinspection SpellCheckingInspection
def inference(input_tensor, train, regularizer):
    with tf.variable_scope('layer1-conv1'):
        conv1_weights = tf.get_variable("weight", [3, 3, 3, 32],
                                        initializer=tf.truncated_normal_initializer(stddev=0.03))
        conv1_biases = tf.get_variable("bias", [32], initializer=tf.constant_initializer(0.0))
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))

    with tf.name_scope("layer2-pool1"):
        pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="VALID")

    with tf.variable_scope("layer3-conv2"):
        conv2_weights = tf.get_variable("weight", [3, 3, 32, 64],
                                        initializer=tf.truncated_normal_initializer(stddev=0.03))
        conv2_biases = tf.get_variable("bias", [64], initializer=tf.constant_initializer(0.0))
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    with tf.name_scope("layer4-pool2"):
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    with tf.variable_scope("layer5-conv3"):
        conv3_weights = tf.get_variable("weight", [3, 3, 64, 128],
                                        initializer=tf.truncated_normal_initializer(stddev=0.03))
        conv3_biases = tf.get_variable("bias", [128], initializer=tf.constant_initializer(0.0))
        conv3 = tf.nn.conv2d(pool2, conv3_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu3 = tf.nn.relu(tf.nn.bias_add(conv3, conv3_biases))

    with tf.name_scope("layer6-pool3"):
        pool3 = tf.nn.max_pool(relu3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    with tf.variable_scope("layer7-conv4"):
        conv4_weights = tf.get_variable("weight", [3, 3, 128, 256],
                                        initializer=tf.truncated_normal_initializer(stddev=0.03))
        conv4_biases = tf.get_variable("bias", [256], initializer=tf.constant_initializer(0.0))
        conv4 = tf.nn.conv2d(pool3, conv4_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu4 = tf.nn.relu(tf.nn.bias_add(conv4, conv4_biases))

    with tf.name_scope("layer8-pool4"):
        pool4 = tf.nn.max_pool(relu4, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    with tf.variable_scope("layer9-conv5"):
        conv5_weights = tf.get_variable("weight", [3, 3, 256, 512],
                                        initializer=tf.truncated_normal_initializer(stddev=0.03))
        conv5_biases = tf.get_variable("bias", [512], initializer=tf.constant_initializer(0.0))
        conv5 = tf.nn.conv2d(pool4, conv5_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu5 = tf.nn.relu(tf.nn.bias_add(conv5, conv5_biases))

    with tf.name_scope("layer10-pool5"):
        pool5 = tf.nn.max_pool(relu5, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

        nodes = 3 * 3 * 512
        reshaped = tf.reshape(pool5, [-1, nodes])

    with tf.variable_scope('layer9-fc1'):
        fc1_weights = tf.get_variable("weight", [nodes, 1024],
                                      initializer=tf.truncated_normal_initializer(stddev=0.03))
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc1_weights))
        fc1_biases = tf.get_variable("bias", [1024], initializer=tf.constant_initializer(0.1))

        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        if train:
            fc1 = tf.nn.dropout(fc1, 0.5)

    with tf.variable_scope('layer10-fc2'):
        fc2_weights = tf.get_variable("weight", [1024, 256],
                                      initializer=tf.truncated_normal_initializer(stddev=0.03))
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc2_weights))
        fc2_biases = tf.get_variable("bias", [256], initializer=tf.constant_initializer(0.1))

        fc2 = tf.nn.relu(tf.matmul(fc1, fc2_weights) + fc2_biases)
        if train:
            fc2 = tf.nn.dropout(fc2, 0.5)

    with tf.variable_scope('layer11-fc3'):
        fc3_weights = tf.get_variable("weight", [256, 64],
                                      initializer=tf.truncated_normal_initializer(stddev=0.03))
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc3_weights))
        fc3_biases = tf.get_variable("bias", [64], initializer=tf.constant_initializer(0.1))

        fc3 = tf.nn.relu(tf.matmul(fc2, fc3_weights) + fc3_biases)
        if train:
            fc3 = tf.nn.dropout(fc3, 0.5)

    with tf.variable_scope('layer12-fc4'):
        fc4_weights = tf.get_variable("weight", [64, category_count],
                                      initializer=tf.truncated_normal_initializer(stddev=0.03))
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc4_weights))
        fc4_biases = tf.get_variable("bias", [category_count], initializer=tf.constant_initializer(0.1))
        fc4 = tf.matmul(fc3, fc4_weights) + fc4_biases

    return fc4


# 定义一个函数，按批次取数据
def minibatches(inputs=None, targets=None, batch_size=None, shuffle=False):
    assert len(inputs) == len(targets)
    indices = np.arange(len(inputs))
    if shuffle:
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batch_size]
        else:
            excerpt = slice(start_idx, start_idx + batch_size)
        yield inputs[excerpt], targets[excerpt]


# read image
data, label = read_img(image_path, image_count)

# 打乱顺序
num_example = data.shape[0]
arr = np.arange(num_example)
np.random.shuffle(arr)
data = data[arr]
label = label[arr]

# 将所有数据分为训练集和验证集
ratio = 0.9
s = np.int(num_example * ratio)
x_train = data[:s]
y_train = label[:s]
x_val = data[s:]
y_val = label[s:]

#
# 占位符
x = tf.placeholder(tf.float32, shape=[None, w, h, c], name='x')
y_ = tf.placeholder(tf.int32, shape=[None, ], name='y_')

# ---------------------------网络结束---------------------------
current_regularizer = tf.contrib.layers.l2_regularizer(regularization_rate)
logits = inference(x, False, current_regularizer)

# (小处理)将logits乘以1赋值给logits_eval，定义name，方便在后续调用模型时通过tensor名字调用输出tensor
b = tf.constant(value=1, dtype=tf.float32)
logits_eval = tf.multiply(logits, b, name='logits_eval')

loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y_, name='loss')
cost = tf.reduce_mean(loss, name='cost')
# train_op = tf.train.AdadeltaOptimizer(learning_rate=learning_rate).minimize(loss)
train_op = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
correct_prediction = tf.equal(tf.cast(tf.argmax(logits, 1), tf.int32), y_)
acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

saver = tf.train.Saver()
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
result = open('result.txt', 'w')
for epoch in range(n_epoch):
    start_time = time.time()
    print("Round %i:" % (epoch + 1))
    result.write("Round %i:\n" % (epoch + 1))
    # training
    train_loss, train_acc, n_batch = 0, 0, 0
    for x_train_a, y_train_a in minibatches(x_train, y_train, current_batch_size, shuffle=True):
        _, err, ac = sess.run([train_op, cost, acc], feed_dict={x: x_train_a, y_: y_train_a})
        train_loss += err
        train_acc += ac
        n_batch += 1
    print("   train loss: %f" % (np.sum(train_loss) / n_batch))
    print("   train acc: %f" % (np.sum(train_acc) / n_batch))
    result.write("   train loss: %f\n" % (np.sum(train_loss) / n_batch))
    result.write("   train acc: %f\n" % (np.sum(train_acc) / n_batch))

    # validation
    val_loss, val_acc, n_batch = 0, 0, 0
    for x_val_a, y_val_a in minibatches(x_val, y_val, current_batch_size, shuffle=False):
        err, ac = sess.run([cost, acc], feed_dict={x: x_val_a, y_: y_val_a})
        val_loss += err
        val_acc += ac
        n_batch += 1
    print("   validation loss: %f" % (np.sum(val_loss) / n_batch))
    print("   validation acc: %f" % (np.sum(val_acc) / n_batch))
    result.write("   validation loss: %f\n" % (np.sum(val_loss) / n_batch))
    result.write("   validation acc: %f\n" % (np.sum(val_acc) / n_batch))
saver.save(sess, model_path)
sess.close()
result.close()
