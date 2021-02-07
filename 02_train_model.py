# -*- coding:utf-8 -*-

import os

import cv2
import numpy as np



import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices("GPU")
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)
    print(tf.config.experimental.get_device_details(gpus[0])['device_name'])



def get_model(width, height, frame_count, outputs):
    base_model = tf.keras.applications.Xception(include_top=False, weights=None, input_shape=(width, height, frame_count), pooling='avg')
    
    output = base_model.output
    output = tf.keras.layers.Dense(outputs, activation=tf.nn.softmax)(output)
    
    model = tf.keras.models.Model(inputs = base_model.input, outputs = output)
    
    model.compile(
        optimizer = tf.keras.optimizers.Adam(),
        loss = tf.keras.losses.CategoricalCrossentropy(),
        metrics = ['accuracy']
    )
    return model



# x, x_w, y, y_h. 这些数据获取自 get_vertices.py
# x, x_w, y, y_h. Get this data from get_vertices.py
x=190
x_w=290
y=30
y_h=230

ROI_WIDTH = x_w - x
ROI_HEIGHT = y_h - y
FRAME_COUNT = 1

MODEL_NAME = 'sekiro.h5'
model = get_model(ROI_WIDTH, ROI_HEIGHT, FRAME_COUNT, outputs=5)
# model.summary()



def roi(img, x, x_w, y, y_h):
    return img[y:y_h, x:x_w]



def train(boss, start, end):
    global model, x, x_w, y, y_h
    for i in range(start, end+1):

        filename = f'training_data-{i}.npy'

        # 加载数据
        # Load data
        train_data = np.load(os.path.join('The_battle_memory', boss, filename), allow_pickle=True)
        print(filename, '总数据量：', len(train_data))

        # 拆分数据和标签
        # Split data and labels
        X = np.array([roi(i[0], x, x_w, y, y_h) for i in train_data]).reshape(-1, ROI_WIDTH, ROI_HEIGHT, FRAME_COUNT)
        Y = np.array([i[1] for i in train_data])
        print('训练数据量：', len(Y))

        # 用 TensorBoard 可视化训练过程
        # Visualize the training process with TensorBoard
        tensorboard = tf.keras.callbacks.TensorBoard(
            log_dir = os.path.join('logs', filename[:-4]),
            histogram_freq = 1,
            update_freq='batch'
        )

        # 模型训练
        # Model training
        model.fit(X, Y, batch_size=16, epochs=3, verbose=1, callbacks=[tensorboard])

        # 保存模型
        # Save model
        model.save(MODEL_NAME)

        # 重新加载模型
        # Reload the model
        model = tf.keras.models.load_model(MODEL_NAME)



boss1 = 'Genichiro_Ashina' # 苇名弦一郎
boss2 = 'Inner_Genichiro'  # 心中的弦一郎
boss3 = 'Inner_Isshin'     # 心中的一心
boss4 = 'Isshin,_the_Sword_Saint' # 剑圣 苇名一心

train(boss1, start=1, end=1)

"""
./The_battle_memory/Genichiro_Ashina
    training_data-1.npy
    training_data-2.npy
    ...
    training_data-100.npy
    
依次读取数据，逐个训练
当然，也可以指定开始和结束的文件
e.g.
    start=15, end=36
怎么选择取决于你。

Read the data in turn and train one by one.
Of course, you can also specify the start and end files.
e.g. 
    start=15, end=36
It's up to you to choose.
"""