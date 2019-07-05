import os  
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import tensorflow as tf
from tensorflow import keras
image_size=(128,128)

from keras import callbacks
from keras.models import Sequential, model_from_yaml, load_model
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPool2D
from keras.optimizers import Adam, SGD
from keras.preprocessing import image
from keras.utils import np_utils, plot_model
from sklearn.model_selection import train_test_split



def load_data():
    path = './data/'
    dir=os.listdir(path)
    images = []
    labels = []
    for labelName in dir:
        labels.append(labelName)
        files=path+labelName+'/'	
        for i in os.listdir(files):
            img_path = files+'/'+i
            img = image.load_img(img_path, target_size=image_size)
            img_array = image.img_to_array(img)
            images.append(img_array)

    data = np.array(images)
    labels = np.array(labels)

    labels = np_utils.to_categorical(labels, 3)
    return data, labels

model = Sequential()

model.add(Conv2D(32, kernel_size=(5, 5), input_shape=(128, 128, 3), activation='relu', padding='same'))
model.add(MaxPool2D())
model.add(Dropout(0.3))

model.add(Conv2D(64, kernel_size=(5, 5), activation='relu', padding='same'))
model.add(MaxPool2D())
model.add(Dropout(0.3))

model.add(Conv2D(128, kernel_size=(5, 5), activation='relu', padding='same'))
model.add(MaxPool2D())
model.add(Dropout(0.5))

model.add(Conv2D(256, kernel_size=(5, 5), activation='relu', padding='same'))
model.add(MaxPool2D())
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(2, activation='softmax'))

model.summary()  #这一句只是输出网络结构

sgd = Adam(lr=0.0003)
model.compile(loss='binary_crossentropy',optimizer=sgd, metrics=['accuracy'])

images, lables = load_data()
images /= 255
x_train, x_test, y_train, y_test = train_test_split(images, lables, test_size=0.2)


print("train.......")
tbCallbacks = callbacks.TensorBoard(log_dir='./logs', histogram_freq=1, write_graph=True, write_images=True)
model.fit(x_train, y_train, batch_size=nbatch_size, epochs=nepochs, verbose=1, validation_data=(x_test, y_test), callbacks=[tbCallbacks])

scroe, accuracy = model.evaluate(x_test, y_test, batch_size=nbatch_size)
print('scroe:', scroe, 'accuracy:', accuracy)

yaml_string = model.to_yaml()
with open('./models/cat_dog.yaml', 'w') as outfile:
    outfile.write(yaml_string)
model.save_weights('./models/cat_dog.h5')
