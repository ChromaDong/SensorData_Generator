import tensorflow as tf
from tensorflow import keras

x = "输入的测试数据"
# 也是二维矩阵 同上

model = keras.models.load_model("路径")

y = model.predict(x)
# 这时候y里面 每一行存放的是模型认为的对应数据的对应各个标签的概率 所以只要排个序 找到最大下标 就可以得到预测出的是哪个标签了
print(y)