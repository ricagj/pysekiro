import os

import cv2
import numpy as np
import pandas as pd


def roi(img, x, x_w, y, y_h):
    return img[y:y_h, x:x_w]


boss1 = 'Genichiro_Ashina' # 苇名弦一郎
boss2 = 'Inner_Genichiro'  # 心中的弦一郎
boss3 = 'Inner_Isshin'     # 心中的一心
boss4 = 'Isshin,_the_Sword_Saint' # 剑圣 苇名一心

boss = boss1
data = np.load(os.path.join('The_battle_memory', boss, f'training_data-{1}.npy'), allow_pickle=True)


Remaining = len(data)

for img, cmd in data:
    
    if   cmd == [1,0,0,0,0]:
        motion = '攻击 | Attack'
    elif cmd == [0,1,0,0,0]:
        motion = '防御 | Deflect'
    elif cmd == [0,0,1,0,0]:
        motion = '垫步 | Step Dodge'
    elif cmd == [0,0,0,1,0]:
        motion = '跳跃 | Jump'
    elif cmd == [0,0,0,0,1]:
        motion = '其他 | Other'
    
    cv2.imshow('img', img)
    
    # x, x_w, y, y_h. 这些数据获取自 getvertices.py
    # x, x_w, y, y_h. Get this data from getvertices.py
    cv2.imshow('roi(img)', roi(img, x=190, x_w=290, y=30, y_h=230))

    Remaining -= 1
    print(f'\r{Remaining:<10}{motion:<15}', end='')
    cv2.waitKey(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
else:
    cv2.destroyAllWindows()
    
# 按 q 停止
# Press 'q' to stop