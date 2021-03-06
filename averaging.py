from pathlib import Path
from tkinter import filedialog
import cv2
import numpy as np

def getFiles():
    dir = ''
    fld = filedialog.askdirectory(initialdir = dir) 

    # Pathオブジェクトを生成
    p = Path(fld)

    # ファイル名の条件指定
    files = list(p.glob("*.tif"))

    return files

def saveImage(image):
    #型変換>16bitグレースケール
    image_Int16 = image.astype(np.uint16)
    
    #平均化した画像の書き出し
    cv2.imwrite('../averaged.tif',image_Int16)


def main():
    #ファイルパスの一覧を取得
    files = getFiles()
    numberOfImages = float(len(files))

    #ファイルをopenCVで読み込み
    images = []
    for file in files:
        image = cv2.imread(str(file),-1)
        #輝度を画像数で割る
        images.append(image/numberOfImages)
    
    #全画像を足し合わせる
    averagesImage = images[0]*0
    for image in images:
        averagesImage += image

    saveImage(averagesImage)

main()

print("End")
