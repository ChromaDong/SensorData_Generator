import tensorflow as tf
from tensorflow import keras
import numpy as np

print("import finished")
def read_and_decode(filename): # 读入tfrecords
    filename_queue = tf.train.string_input_producer([filename],shuffle=True)#生成一个queue队列
 
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)#返回文件名和文件
    features = tf.parse_single_example(serialized_example,
                                       features={
                                           'label': tf.FixedLenFeature([], tf.int64),
                                           'img_raw' : tf.FixedLenFeature([], tf.string),
                                       })#将image数据和label取出来
 
    img = tf.decode_raw(features['img_raw'], tf.uint8)
    img = tf.reshape(img, [128, 128, 3])  #reshape为128*128的3通道图片
    img = tf.cast(img, tf.float32) * (1. / 255) - 0.5 #在流中抛出img张量
    label = tf.cast(features['label'], tf.int32) #在流中抛出label张量
    sess = tf.Session()
    print(img)
    print(label)
    np_img=np.array(img)
    np_label=np.array(label)
    return np_img, np_label

def my_read_dataset(filename):
	filename='./data.tfrecords'
	dataset=record_iterator = tf.python_io.tf_record_iterator(path=filename)

	for string_record in record_iterator:
		example = tf.train.Example()
		example.ParseFromString(string_record)
		print(example)
		# Exit after 1 iteration as this is purely demonstrative.
		break

def myReadDataset(filename):
	filenames = [filename]
	raw_dataset = tf.data.TFRecordDataset(filenames)
	raw_dataset
	print(raw_dataset)
my_read_dataset('123')
myReadDataset('./data.tfrecords')
print("Defined finished")

print("# 二维矩阵 每一行是一个样本 列数为样本个数")


print("start to read dataset and decode...")

x,y=read_and_decode("./data.tfrecord")

print("二维矩阵 每一行是对应样本取到该分类的概率 形如[0,...,0,1,0,...,0] 列数为样本个数 现假设样本有10个分类 那么列数就是10")

print("start define model")

model = keras.Sequential([
	keras.layers.Flatten(input_shape=(128, 128)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(3, activation=tf.nn.softmax)
	])

print("32为该层神经元个数 activation为激活函数")

'''
model.add(keras.layers.Dense(32, activation="sigmoid"))
model.add(keras.layers.Dense(16, activation="sigmoid"))
model.add(keras.layers.Dense(12, activation="softplus"))
model.add(keras.layers.Dense(10, activation="softmax"))  
'''

print("最后输出长度为10的向量")

print("Start compline")

model.compile(optimizer=keras.optimizers.Adam(0.0001),
              loss="categorical_crossentropy", metrics=['accuracy'])

print("编译模型 使用Adam优化器 如果用梯度下降可以改成 keras.optimizers.SGD 0.01是学习速率 损失函数是交叉熵")

print("start to train")

model.fit(x, y, eopchs=10, batch_size=20)
# 训练模型 一共20步 采用随机小批量 批量个数为20
print("train finished")

print("save model")

model.save("./")
