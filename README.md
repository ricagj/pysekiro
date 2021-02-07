## Using Python programming to Play 《Sekiro™ Shadows Die Twice》

# Reference
https://github.com/Sentdex/pygta5  
https://github.com/analoganddigital/sekiro_tensorflow  
https://github.com/analoganddigital/DQN_play_sekiro

# Preparation

#### Install Anaconda3 first
https://www.anaconda.com/

#### Create a virtual environment and install dependencies
~~~shell
conda create -n pysekiro python=3.8
conda activate pysekiro
conda install pandas
conda install pywin32
pip install opencv-python>=4.0
pip install tensorflow>=2.0
~~~

# 教程 | Tutorial
#### 激活环境 | Activate the environment
~~~shell
conda activate pysekiro
~~~

### 数据预览 | Preview data
~~~shell
python .\00_preview_data.py
~~~
![preview data](./00_preview_data.gif)

### 收集数据 | Collect data
![collect data](./01_collect_data.gif)
- Some game settings
    - 打开游戏 《只狼：影逝二度》
        - 设定
            - 按键设置
                - 攻击动作
                    - 攻击    键盘    J
                    - 防御    键盘    K
            - 图像设定
                - 屏幕模式    窗口
                - 屏幕分辨率    1280 x 720
    - Open the game 《Sekiro™ Shadows Die Twice》
        - Options
            - Key Config
                - Attack Action
                    - Attack    keyboard    J
                    - Deflect, (Hold) Gurad    keyboard    K
            - Graphics Options
                - Screen Mode    Windowed
                - Screen Resolution    1280 x 720
- 说明 | Description
    - 按 ‘T’ 开始 | Press 'T' to start.
    - 按 ‘T’ 暂停\继续 | You can also press 'T' to pause or continue.
    - 按 ‘P’ 结束并保存 | Press 'P' to stop and save.

~~~shell
python .\01_collect_data.py
~~~

### 训练模型 | Train_model
~~~shell
python .\02_train_model.py
~~~

在等待的过程中，我们可以打开 TensorBoard 来可视化训练过程。  
While waiting, we can open tensorboard to visualize the training process.  
~~~ 
tensorboard --logdir=.\logs
~~~
点击 http://localhost:6006/ 进入 TensorBoard。  
Click http://localhost:6006/ to enter TensorBoard.  

### 测试模型 | Test model
~~~shell
python .\03_test_model.py
~~~
- 说明 | Description
    - 按 ‘T’ 开始 | Press 'T' to start.
    - 按 ‘T’ 暂停\继续 | You can also press 'T' to pause or continue.
    - 按 ‘P’ 结束并保存 | Press 'P' to stop and save.

### getvertices.py
~~~shell
python .\getvertices.py
~~~
![demo_01](./demo_01.gif)  
![demo_02](./demo_02.gif)  
在弹出来的窗口中按顺序依次点击左下，左上，右上，右下，然后按键盘上的“ESC”键。  
In the pop-up window, click bottom left, top left, top right, bottom right in order, and then press the "ESC" key on the keyboard.  

我们可以用它来获取人物的状态，例如HP，躯干。  
We can use it to get the status of the character, such as HP, posture.

~~~shell
python .\getstatus.py
~~~
![getstatus](./getstatus.gif) 
