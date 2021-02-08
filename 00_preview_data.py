# -*- coding:utf-8 -*-

from getvertices import *

# ---*---

boss = 'Genichiro_Ashina' # 苇名弦一郎
data = np.load(os.path.join('The_battle_memory', boss, f'training_data-{1}.npy'), allow_pickle=True)
Remaining = len(data)

# ---*---

# x, x_w, y, y_h. 这些数据获取自 getvertices.py
# x, x_w, y, y_h. Get this data from getvertices.py
x=190
x_w=290
y=30
y_h=230

# ---*---

print('Press "q" to quit. ') # 按q键离开。

for img, cmd in data:
    
    if   cmd == [1,0,0,0,0]:
        motion = 'Attack'     # 攻击
    elif cmd == [0,1,0,0,0]:
        motion = 'Deflect'    # 弹反
    elif cmd == [0,0,1,0,0]:
        motion = 'Step Dodge' # 垫步
    elif cmd == [0,0,0,1,0]:
        motion = 'Jump'       # 跳跃
    elif cmd == [0,0,0,0,1]:
        motion = 'O'      # 其他
    
    cv2.imshow('img', img)
    cv2.imshow('roi(img)', roi(img, x, x_w, y, y_h))

    Remaining -= 1
    print(f'\r{Remaining:<6}{motion:<11}', end='')
    cv2.waitKey(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
else:
    cv2.destroyAllWindows()
    
# 按 q 停止
# Press 'q' to stop