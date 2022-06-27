# get3Dcoordinate_fromD435
## Purpose  
Get 3D coorinate from Realsense D435
program実行後に表示されたRGB画像上でカーソルをクリックした箇所の三次元座標[m]（D435を原点）を取得する  
なお、RGB画像とdepthの画角のサイズは合わせている
## How to use  
### Ready  
Realsense D435, PC
まだrelasense をpythonで動かす準備をしたことない人はpipでpyrealsense をインストールするなりして下さい  
```
pip3 install pyrealsense2
```
### Use  
terminalを立ち上げて以下のcommandを実行
```
python3 get3Dcoordinate_fromD435.py
```
## Problem  
D435の精度の問題なのか Fig.1のように写っている手の左側に紺色の影ができており、この領域では3D座標が取得できない（どうにかしたいね）  
![alt text](https://github.com/yoshi0815/get3Dcoordinate_fromD435/blob/main/errorBig.png "Title Text1")
対処法?としては Fig.2のようにカメラとオブジェクト間の距離を離すことで計測付加領域を小さくできる  
![alt text](https://github.com/yoshi0815/get3Dcoordinate_fromD435/blob/main/errorSmall.png "Logo Title Text2")
## Reference  
https://qiita.com/tom_eng_ltd/items/635414ff0b43e1c506f6  
https://qiita.com/hoshianaaa/items/b0caef7b4738b00d6d7d  
