from pathlib import Path
from tkinter import filedialog
import cv2
import numpy as np
import csv

def getFiles():
    dir = ''
    fld = filedialog.askdirectory(initialdir = dir) 

    # Pathオブジェクトを生成
    p = Path(fld)

    # ファイル名の条件指定
    files = list(p.glob("*.tif"))

    return files

def saveImage(image, filepath):
    #型変換>16bitグレースケール
    image_Int16 = image.astype(np.uint16)
    
    #平均化した画像の書き出し
    cv2.imwrite(filepath,image_Int16)

    return

def getCropSize():
    filename = filedialog.askopenfilename()
    with open(filename) as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    x, width, y, hight = int(l[0][1]), int(l[1][1]), int(l[2][1]), int(l[3][1])
    #targetsize = {"x":l[0][1], "width" :l[1][1], "y":l[2][1], "hight" :l[3][1]}
  
    return x, width, y, hight

def main():
    #ファイルパスの一覧を取得
    files = getFiles()
    #画像の切り出しサイズパラメータを取得
    x, width, y, hight = getCropSize()

    #ファイルをopenCVで読み込み
    for file in files:
        image = cv2.imread(str(file),-1)
        #画像を切り出す
        cropped_image = image[y:y + hight, x:x + width]

        #切り出しごとのファイル名を作る
        folder = file.parent.resolve()
        filename = file.stem
        filepath = str(folder) + '/' + str(filename) + '-cropped.tif'

        #画像を保存する
        saveImage(cropped_image, filepath)
   
 
main()

print("End")