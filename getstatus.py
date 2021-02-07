from getvertices import *



boss = 'Genichiro_Ashina' # 苇名弦一郎
data = np.load(os.path.join('The_battle_memory', boss, f'training_data-1.npy'), allow_pickle=True)



Remaining = len(data)

print('按q键离开。 | Press "q" to quit. ')

for img, cmd in data:
    
    if   cmd == [1,0,0,0,0]:
        motion = '攻击'
    elif cmd == [0,1,0,0,0]:
        motion = '防御'
    elif cmd == [0,0,1,0,0]:
        motion = '垫步'
    elif cmd == [0,0,0,1,0]:
        motion = '跳跃'
    elif cmd == [0,0,0,0,1]:
        motion = '其他'
    
    cv2.imshow('img', img)
    cv2.imshow('roi(img)', roi(img, x=190, x_w=290, y=30, y_h=230))
    
    cv2.imshow('GrabCut_ROI(img)', GrabCut_ROI(img, [np.array([[185, 235], [145, 15], [335, 15], [295, 235]], np.int32)]))
    cv2.imshow('GrabCut_ROI. 我方血条 | HP | Vitality', GrabCut_ROI(img, [np.array([[26, 247], [26, 243], [185, 243], [185, 247]], np.int32)]))
    cv2.imshow('GrabCut_ROI. 我方躯干 | Posture', GrabCut_ROI(img, [np.array([[185, 235], [185, 233], [295, 233], [295, 235]], np.int32)]))
    cv2.imshow('GrabCut_ROI. 敌方血条 | Boss HP | Boss Vitality', GrabCut_ROI(img, [np.array([[26, 27], [26, 24], [133, 24], [133, 27]], np.int32)]))
    cv2.imshow('GrabCut_ROI. 敌方躯干 | Boss Posture', GrabCut_ROI(img, [np.array([[145, 17], [145, 15], [335, 15], [335, 17]], np.int32)]))
    
    Remaining -= 1
    print('\r{:<10}{:<20}'.format(Remaining, motion), end='')
    cv2.waitKey(1)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
else:
    cv2.destroyAllWindows()