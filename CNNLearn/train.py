from tensorflow import keras


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
 
    return img, label

x = "训练样本"  # 二维矩阵 每一行是一个样本 列数为样本个数
y = "训练样本对应标签"

x,y=read_and_decode("./data.tfrecord")


# 二维矩阵 每一行是对应样本取到该分类的概率 形如[0,...,0,1,0,...,0] 列数为样本个数 现假设样本有10个分类 那么列数就是10
model = keras.Sequential()

# 32为该层神经元个数 activation为激活函数
model.add(keras.layers.Dense(32, activation="sigmoid"))
model.add(keras.layers.Dense(16, activation="sigmoid"))
model.add(keras.layers.Dense(12, activation="softplus"))
model.add(keras.layers.Dense(10, activation="softmax"))  # 最后输出长度为10的向量

model.compile(optimizer=keras.optimizers.Adam(0.0001),
              loss="categorical_crossentropy", metrics=['accuracy'])
# 编译模型 使用Adam优化器 如果用梯度下降可以改成 keras.optimizers.SGD 0.01是学习速率 损失函数是交叉熵

model.fit(x, y, eopchs=10, batch_size=20)
# 训练模型 一共20步 采用随机小批量 批量个数为20

model.save("./")
