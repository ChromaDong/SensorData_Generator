import os 
import tensorflow as tf 
import numpy as np
#cwd='./data/train/'

# First import library
import pyrealsense2 as rs
# Import Numpy for easy array manipulation
import numpy as np
# Import OpenCV for easy image rendering
import cv2
# Import argparse for command-line options
import argparse
# Import os.path for file path manipulation
import os.path

cwd='./rawData/'
classes={'bow','sit','stand'}  #人为设定2类
#writer= tf.python_io.TFRecordWriter("dog_and_cat_train.tfrecords") #要生成的文件
writer = tf.python_io.TFRecordWriter("data.tfrecords") #要生成的文件

for index,name in enumerate(classes):
    bagPath=cwd+name+'/'
	#Create pipeline
	pipeline = rs.pipeline()
	# Create a config object
	config = rs.config()
	# Tell config that we will use a recorded device from filem to be used by the pipeline through playback.
	rs.config.enable_device_from_file(config, bagPath)
	# Configure the pipeline to stream the depth stream
	config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)

	# Start streaming from file
	pipeline.start(config)
	frames = pipeline.wait_for_frames()
    example = tf.train.Example(features=tf.train.Features(feature={
        "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
        'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[frame]))
        })) #example对象对label和image数据进行封装
    writer.write(example.SerializeToString())  #序列化为字符串
writer.close()
