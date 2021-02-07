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

# Tutorial

### Preview data
![preview data](./00_preview_data.gif)

### Collect data
![collect data](./01_collect_data.gif)
- Description
    - 按 ‘T’ 开始 | Press 'T' to start
    - 按 ‘T’ 暂停\继续 | You can also press 'T' to pause or continue.
    - 按 ‘P’ 结束并保存 | Press 'P' to stop and save.
