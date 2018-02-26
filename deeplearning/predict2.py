from skimage import io,transform
import tensorflow as tf
import numpy as np


path1 = "C:/Users/bunny/Desktop/dataset1/root/fat/ffffc643bde49df27bb9108a872eaa4d43c553e2.jpg"
path2 = "C:/Users/bunny/Desktop/dataset1/root/parenchyma/ffff220048fbcf2d65868e6f03c99e5c50a35acb.jpg"
path3 = "C:/Users/bunny/Desktop/dataset1/root/tumor/fffef82b1eff6f6a0b240e0b447195986ba12de6.jpg"
path4 = "C:/Users/bunny/Desktop/dataset1/sample/fat/2f22acc328f653580d4ac647895618e3f1e9c436.jpg"
path5 = "C:/Users/bunny/Desktop/dataset1/sample/parenchyma/0e30a838c5d5ddf41d11bc7c8c8314b4820906cb.jpg"
path6 = "C:/Users/bunny/Desktop/dataset1/sample/tumor/0b3160606c517085f2924c10411431a32c7d3c35.jpg"

name_dict = {0:'fat',1:'parenchyma',2:'tumor'}

w=100
h=100
c=3

def read_one_image(path):
    img = io.imread(path)
    img = transform.resize(img,(w,h))
    return np.asarray(img)

sess=tf.InteractiveSession()  
sess.run(tf.global_variables_initializer())
data = []
data1 = read_one_image(path1)
data2 = read_one_image(path2)
data3 = read_one_image(path3)
data4 = read_one_image(path4)
data5 = read_one_image(path5)    
data6 = read_one_image(path6)
data.append(data1)
data.append(data2)
data.append(data3)
data.append(data4)
data.append(data5)
data.append(data6) 

path='c:/Users/bunny/Desktop/dataset1/root/'
model_path='c:/Users/bunny/Desktop/dataset1/root/model.ckpt.meta'
saver = tf.train.import_meta_graph(model_path)
saver.restore(sess,tf.train.latest_checkpoint(path))

graph = tf.get_default_graph()
x = graph.get_tensor_by_name("x:0")
feed_dict = {x:data}

logits = graph.get_tensor_by_name("logits_eval:0")

classification_result = sess.run(logits,feed_dict)

#打印出预测矩阵
print(classification_result)
#打印出预测矩阵每一行最大值的索引
print(tf.argmax(classification_result,1).eval())
#根据索引通过字典对应花的分类
output = []
output = tf.argmax(classification_result,1).eval()
for i in range(len(output)):
    print("Picture",i+1,":"+name_dict[output[i]])

sess.close()