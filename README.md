## Using Python programming to Play 《Sekiro™ Shadows Die Twice》

<p align="center">
    <a>English</a>
    | 
    <a href="https://github.com/ricagj/pysekiro/blob/main/README_CN.md">中文</a>
</p>

#### total 76.4 MB

# Reference
https://github.com/Sentdex/pygta5  
https://github.com/analoganddigital/sekiro_tensorflow  

# Description

Through this program, you will learn how to collect your own data set with python, train and test your own model with tensorflow.  

1. The core of this program is supervised learning with images as training data and keypress records as labels.  
2. Use python to get the screen image in real time and your keypress record at that moment.  
3. In the training process, the image is passed into the neural network as input, and the neural network outputs its corresponding keys.  
4. Then during the test, the program captures the screen image in real time and enters it into the neural network, calculates the corresponding keys, and outputs it to the keyboard.  
5. It is essentially an image classification, which divides the images into several categories according to the keypress records.  

This version ends here. The power of supervised learning is ultimately limited. Training game AI really still needs reinforcement learning. But since I have a weak foundation in reinforcement learning and I am still learning, it may take some time.  

Finally, thanks to Sentdex and analoganddigital, thanks to them I was able to complete this program.  

# Next Version
https://github.com/ricagj/pysekiro_with_RL  

# Model weights have been uploaded ( sekiro_weights.h5 )
For those who want to see the results directly, you can run 03_test_model.py directly.  
However, the model currently has only basic combat capabilities, and has no strength to defeat the target, Shunichiro Ashina.  

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

# Tutorial

#### Activate the environment
~~~shell
conda activate pysekiro
~~~

## Preview data
~~~shell
python .\00_preview_data.py
~~~
![preview data](./Toturial_gif/00_preview_data.gif)  

## Collect data
- Some game settings
    - Open the game 《Sekiro™ Shadows Die Twice》
        - Options
            - Key Config
                - Attack Action
                    - Attack    keyboard    J
                    - Deflect, (Hold) Gurad    keyboard    K
            - Graphics Options
                - Screen Mode    Windowed
                - Screen Resolution    1280 x 720
- Description
    - Press 'T' to start.
    	- Press 'T' to pause or continue.
    - Press 'P' to stop and save.

~~~shell
python .\01_collect_data.py
~~~
![collect data](./Toturial_gif/01_collect_data.gif)  
log in .\The_battle_memory_of_Genichiro_Ashina.txt  

## Train_model
~~~shell
python .\02_train_model.py
~~~

While waiting, we can open tensorboard to visualize the training process.  
~~~ 
tensorboard --logdir=.\logs
~~~
Click http://localhost:6006/ to enter TensorBoard.  

## Test model
~~~shell
python .\03_test_model.py
~~~
- Description
    - Press 'T' to start.
    - You can also press 'T' to pause or continue.
    - Press 'P' to stop.

## getvertices.py
~~~shell
python .\getvertices.py
~~~
![demo_01](./Toturial_gif/demo_01.gif)  
In the pop-up window, click bottom left, top left, top right, bottom right in order, and then press the "ESC" key on the keyboard.  

We can use it to get the status of the character, such as HP, posture.  

##### Get Sekiro HP
![get_Sekiro_HP](./Toturial_gif/get_Sekiro_HP.gif)  
##### Get Sekiro Posture
![get_Sekiro_Posture](./Toturial_gif/get_Sekiro_Posture.gif)  
##### Get Boss HP
![get_Boss_HP](./Toturial_gif/get_Boss_HP.gif)  
##### Get Boss Posture
![get_Boss_Posture](./Toturial_gif/get_Boss_Posture.gif)  