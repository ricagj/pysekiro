## 用python玩《只狼：影逝二度》

<p align="center">
    <a href="https://github.com/ricagj/pysekiro/blob/main/README.md">English</a>
    | 
    <a>中文</a>
</p>

# 参考
https://github.com/Sentdex/pygta5  
https://github.com/analoganddigital/sekiro_tensorflow  

# 说明

通过这个程序，你将了解如何用python搜集属于自己的数据集，用tensorflow训练并测试自己的模型。  

1. 本程序的核心就是以图像为训练数据，以按键记录为标签的监督学习。  
2. 用python实时获取屏幕图像还有那一瞬间你的按键记录。  
3. 在训练的过程中，把图像作为输入传入神经网络，神经网络输出为其对应的按键。  
4. 然后在测试的过程中，程序实时捕获屏幕图像输入神经网络，计算出对应的按键再输出到键盘上。  
5. 本质上就是个图像分类，把图像按照按键记录分成几个类。  

这个版本就到此结束了，监督学习的力量终究是有限的，训练游戏AI果然还是要用到强化学习的。但由于我强化学习的基础比较薄弱，还在学习中，所以可能需要一些时间。  

最后，鸣谢一下 Sentdex 和 analoganddigital，多亏了他们我才能完成这个程序。  

# 下一个版本
https://github.com/ricagj/pysekiro_with_RL  

# 准备

#### 先安装 Anaconda3
https://www.anaconda.com/  

#### 创建虚拟环境和安装依赖
~~~shell
conda create -n pysekiro python=3.8
conda activate pysekiro
conda install pandas
conda install pywin32
pip install opencv-python>=4.0
pip install tensorflow>=2.0
~~~

# 教程

#### 激活环境
~~~shell
conda activate pysekiro
~~~

## 数据预览
~~~shell
python .\00_preview_data.py
~~~
![preview data](./Toturial_gif/00_preview_data.gif)  

## 收集数据
- 一些游戏设置
    - 打开游戏 《只狼：影逝二度》
        - 设定
            - 按键设置
                - 攻击动作
                    - 攻击    键盘    J
                    - 防御    键盘    K
            - 图像设定
                - 屏幕模式    窗口
                - 屏幕分辨率    1280 x 720
- 说明
    - 按 ‘T’ 开始
        - 按 ‘T’ 暂停\继续
    - 按 ‘P’ 结束并保存

~~~shell
python .\01_collect_data.py
~~~
![collect data](./Toturial_gif/01_collect_data.gif)  
日志在 .\The_battle_memory_of_Genichiro_Ashina.txt  

## 训练模型
~~~shell
python .\02_train_model.py
~~~

在等待的过程中，我们可以打开 TensorBoard 来可视化训练过程。   
~~~ 
tensorboard --logdir=.\logs
~~~
点击 http://localhost:6006/ 进入 TensorBoard。  

## 测试模型
~~~shell
python .\03_test_model.py
~~~
- Description
    - Press 'T' to start.
    - You can also press 'T' to pause or continue.
    - Press 'P' to stop and save.

## getvertices.py
~~~shell
python .\getvertices.py
~~~
![demo_01](./Toturial_gif/demo_01.gif)  
在弹出来的窗口中按顺序依次点击左下，左上，右上，右下，然后按键盘上的“ESC”键。  

我们可以用它来获取人物的状态，例如HP，躯干。  

##### 获取 只狼 HP
![get_Sekiro_HP](./Toturial_gif/get_Sekiro_HP.gif)  
##### 获取 只狼 架势
![get_Sekiro_Posture](./Toturial_gif/get_Sekiro_Posture.gif)  
##### 获取 Boss HP
![get_Boss_HP](./Toturial_gif/get_Boss_HP.gif)  
##### 获取 Boss 架势
![get_Boss_Posture](./Toturial_gif/get_Boss_Posture.gif)  