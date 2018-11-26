 # -*- coding:utf-8 -*-
import numpy
import cv2
cascade_path = './haarcascade_frontalface_alt.xml'

def ReadImage():
    for i in range(1, 17):
        filename = "img" + "%d.jpg" % i
        
        #ファイル読み込み
        image = cv2.imread(filename)
        #グレースケール変換
        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        #カスケード分類器の特徴量を取得する
        cascade = cv2.CascadeClassifier(cascade_path)
        #物体認識（顔認識）の実行
        facerect = cascade.detectMultiScale(
                        image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
        
        print(filename) 
        print(len(facerect))
        
        if len(facerect) <= 0:
            continue
        
        rect = facerect[0]
        for r in facerect:
            if rect[2] < r[2]:
                rect = r
            
        
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        
        # img[y: y + h, x: x + w] 
        cv2.imwrite('face_' + filename, image_gray[y:y+h, x:x+w])

if __name__ == '__main__':
    ReadImage()