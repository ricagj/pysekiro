# -*- coding:utf-8 -*-

import os
import shutil
import time

import cv2
import numpy as np

from getkeys import key_check
from grabscreen import grab_screen



j  = [1,0,0,0,0] # 攻击 | Attack
k  = [0,1,0,0,0] # 防御 | Deflect
ls = [0,0,1,0,0] # 垫步 | Step Dodge
sp = [0,0,0,1,0] # 跳跃 | Jump
ot = [0,0,0,0,1] # 其他 | Other

def keys_to_output(keys):
    output = [0,0,0,0,0]

    if   'J' in keys:
        output = j
        motion = '攻击 | Attack'
    elif 'K' in keys:
        output = k
        motion = '防御 | Deflect'
    elif 'LSHIFT' in keys:
        output = ls
        motion = '垫步 | Step Dodge'
    elif 'SPACE' in keys or ('K' in keys and 'J' in keys):    # 'K' + 'J' = 'Sakura Dance' ≈ jump
        output = sp
        motion = '跳跃 | Jump'
    else:
        output = ot
        motion = '其他 | Other'
    return output, motion



# find_max_num() 和 merge_data() 是保存数据时用的代码
# find_max_num() and merge_data() are the codes used when saving data 
def find_max_num(path):
    filenames = os.listdir(path)
    if 'training_data-1.npy' in filenames:
        max_num = max([int(x[14:-4]) for x in filenames if '.npy' in x])
    else:
        max_num = 0
    return max_num

def merge_data(boss):
    path_1 = 'tmp_data'
    max_num_1 = find_max_num(path_1)
    if max_num_1 <= 1:
        print('There is no data to merge.')
        shutil.rmtree(path_1)
        return -1
    
    npy_file = os.path.join(path_1, 'training_data-1.npy')
    data = np.load(npy_file, allow_pickle=True)
    for i in range(2, max_num_1 + 1):
        npy_file = os.path.join(path_1, f'training_data-{i}.npy')
        next_data = np.load(npy_file, allow_pickle=True)
        
        data = np.append(data, next_data, axis=0)
    
    path_2 = os.path.join('The_battle_memory', boss)

    max_num_2 = find_max_num(path_2)
    np.save(os.path.join(path_2, f'training_data-{max_num_2+1}.npy'), data)
    
    shutil.rmtree(path_1)



# 游戏窗口大小
GAME_WIDTH = 1280
GAME_HEIGHT = 720

# 标准窗口大小
STANDARD_WIDTH = 480
STANDARD_HEIGHT = 270

def battle_with_(boss):
    
    starting_value = 1
    training_data = []
    battle_logs = []
    
    path_1 = 'tmp_data'
    if path_1 not in os.listdir():
        os.mkdir(path_1)
    
    save_path = os.path.join(path_1, f'training_data-{starting_value}.npy')
    
    print('Ready!')

    paused = True
    while True:
        
        if not paused:
            last_time = time.time()
            
            # 屏幕捕获，并图像缩放
            # Grab screen, and resize the image
            screen = grab_screen(region = (0, 30, GAME_WIDTH, GAME_HEIGHT+30))
            screen = cv2.resize(screen, (STANDARD_WIDTH, STANDARD_HEIGHT))
            
            # 按键检测
            # key check
            keys = key_check()
            output, motion = keys_to_output(keys)
            
            # 数据整合
            # data integration
            training_data.append([screen, output])
            
            # 临时保存数据
            # Save data temporarily
            if len(training_data) == 100:
                np.save(save_path, training_data)
                training_data = []
                starting_value += 1
                save_path = os.path.join(path_1, f'training_data-{starting_value}.npy')
            
            # 记录战斗数据
            # Record combat data
            battle_log = f'loop took {round(time.time()-last_time, 3):>5} seconds. motion {motion:<18}. keys {str(keys):<35}'
            battle_logs.append(battle_log+'\n')
            print('\r'+battle_log, end='')
        
        # 再次检测按键
        # key check again
        keys = key_check()
        
        # 按 ‘T’ 暂停或继续
        # Press 'T' to pause or continue
        if 'T' in keys:
            if paused:
                paused = False
                print('\nstarting!')
                time.sleep(1)
            else:
                paused = True
                print('\nPausing!')
                time.sleep(1)
        
        # 按 ‘P’ 结束并保存
        # Press 'P' to stop and save
        if 'P' in keys:
            np.save(save_path, training_data)
            break
    
    print('\n\nstop, please wait')
    
    # 合并临时数据
    # Merge temporary data
    merge_data(boss)
    
    # 写入战斗数据到txt
    # Write battle data to TXT
    with open(f'The battle memory of {boss}.txt', 'a+') as log:
        log.write('\n\n\n\n\n')
        for log_data in battle_logs:
            log.write(log_data)

    print('done!')


if __name__ == '__main__':
    boss1 = 'Genichiro_Ashina' # 苇名弦一郎
    boss2 = 'Inner_Genichiro'  # 心中的弦一郎
    boss3 = 'Inner_Isshin'     # 心中的一心
    boss4 = 'Isshin,_the_Sword_Saint' # 剑圣 苇名一心
    
    battle_with_(boss1)