# -*- coding:utf-8 -*-

import time
import random

import cv2
import numpy as np

from directkeys import PressKey,ReleaseKey, W, J, K, LSHIFT, SPACE
from getkeys import key_check
from getvertices import roi
from grabscreen import grab_screen

# ---*---

import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices("GPU")
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)
    print(tf.config.experimental.get_device_details(gpus[0])['device_name'])

# ---*---

def ReleaseAllKey():
    ReleaseKey(J)
    ReleaseKey(K)
    ReleaseKey(LSHIFT)
    ReleaseKey(SPACE)
    ReleaseKey(W)

def Attack():
    PressKey(W)
    PressKey(J)
    time.sleep(0.1)
    ReleaseAllKey()

def Deflect():
    PressKey(W)
    PressKey(K)
    time.sleep(0.05)
    ReleaseAllKey()

def Stop_Dodge():
    PressKey(W)
    PressKey(LSHIFT)
    time.sleep(0.05)
    ReleaseAllKey()

def Jump():
    PressKey(W)
    PressKey(SPACE)
    time.sleep(0.05)
    ReleaseAllKey()

# ---*---

MODEL_NAME = 'sekiro.h5'
model = tf.keras.models.load_model(MODEL_NAME)

# ---*---

GAME_WIDTH = 1280
GAME_HEIGHT = 720

# x, x_w, y, y_h. 这些数据获取自 getvertices.py
# x, x_w, y, y_h. Get this data from getvertices.py
x=190
x_w=290
y=30
y_h=230

ROI_WIDTH = x_w - x
ROI_HEIGHT = y_h - y

# 标准窗口大小
STANDARD_WIDTH = 480
STANDARD_HEIGHT = 270

FRAME_COUNT = 1

def main():
    global model, x, x_w, y, y_h
    print('Ready!')
    
    paused = True

    while True:
        
        if not paused:
            
            last_time = time.time()
            
            # 屏幕捕获，并图像缩放
            # Grab screen, and resize the image
            screen = grab_screen(region=(0, 30, GAME_WIDTH, GAME_HEIGHT+30))
            screen = cv2.resize(screen, (STANDARD_WIDTH, STANDARD_HEIGHT))

            # 提取ROI, 然后输入模型进行预测
            # Extract ROI, then input the model to predict
            screen = roi(screen, x, x_w, y, y_h)
            prediction = model.predict([screen.reshape(-1, ROI_WIDTH, ROI_HEIGHT, FRAME_COUNT)])[0]

            WEIGHTS = [1.0, 1.0, 1.0, 1.0, 0.01]
            prediction = np.array(prediction) * np.array(WEIGHTS)
            
            mode_choice = np.argmax(prediction)
                
            if   mode_choice == 0:
                choice_picked = 'Attack'     # 攻击
                Attack()

            elif mode_choice == 1:
                choice_picked = 'Deflect'    # 弹反
                Deflect()

            elif mode_choice == 2:
                choice_picked = 'Step Dodge' # 垫步
                Stop_Dodge()

            elif mode_choice == 3:
                choice_picked = 'Jump'       # 跳跃
                Jump()

            elif mode_choice == 4:
                choice_picked = 'O'      # 其他
            
            print(f'\rLoop took {round(time.time()-last_time, 3):>5} seconds. Choice: {choice_picked:<11}', end='')
        
        # 再次检测按键
        # key check again
        keys = key_check()

        # 按 ‘T’ 暂停或继续
        # Press 'T' to pause or continue
        if 'T' in keys:
            if paused:
                paused = False
                print('\nStarting!')
                time.sleep(1)
            else:
                paused = True
                print('\nPausing!')
                time.sleep(1)
        
        # 按 ‘P’ 结束
        # Press 'P' to stop
        if 'P' in keys:
            cv2.destroyAllWindows()
            break
    
    print('\nDone!')

# ---*---

main() 