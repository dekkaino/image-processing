def writeCSV():
    import pandas as pd

    dataset = pd.read_csv('iris.csv', index_col=0)
    filename = 'iris_new'

    for i in range(10):
        tempname = filename + str(i)
        print(tempname)
        dataset.to_csv(tempname + '.csv')  # csv ファイルとして保存

def getFiles():
    from pathlib import Path
    from tkinter import filedialog

    dir = ''
    fld = filedialog.askdirectory(initialdir = dir) 

    # Pathオブジェクトを生成
    p = Path(fld)

    # ファイル名の条件指定
    files = list(p.glob("*.tif"))

    return files


def main():
    import cv2
    import numpy as np
    
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

    #型変換>16bitグレースケール
    averagesImage_Int16 = averagesImage.astype(np.uint16)
    
    #平均化した画像の書き出し
    cv2.imwrite('averaged.tif',averagesImage_Int16)

main()

print("End")