import sys
sys.path.append('/usr/local/Cellar/opencv/3.4.1_5/lib/python3.6/site-packages')
import cv2


def human():

    # 入力画像の読み込み
    img = cv2.imread("input3.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # HoG特徴量 + SVMで人の識別器を作成
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05}

    # 作成した識別器で人を検出
    human, r = hog.detectMultiScale(gray, **hogParams)

    # 人の領域を赤色の矩形で囲む
    for (x, y, w, h) in human:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,250,), 3)

    # 結果を出力
    cv2.imwrite("result3.jpg",img)

def matching_featurepoint():
    
    img1 = cv2.imread("test01.jpg")
    # 画像２
    img2 = cv2.imread("test02.jpg")

    # A-KAZE検出器の生成
    akaze = cv2.ORB_create()                  

    # 特徴量の検出と特徴量ベクトルの計算
    kp1, des1 = akaze.detectAndCompute(img1, None)
    kp2, des2 = akaze.detectAndCompute(img2, None)

    # Brute-Force Matcher生成
    bf = cv2.BFMatcher()

    # 特徴量ベクトル同士をBrute-Force＆KNNでマッチング
    matches = bf.knnMatch(des1, des2, k=2)

    # データを間引きする
    ratio = 0.8
    good = []
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good.append([m])

    # 対応する特徴点同士を描画
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

    print(len(good))
    # 画像表示
    cv2.imwrite("result1.jpg",img3)
    cv2.imshow('img', img3)

    # キー押下で終了
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_featurepoint():
    # 画像ファイルの読み込み
    img = cv2.imread('img1.jpg')

    # ORB (Oriented FAST and Rotated BRIEF)
    detector = cv2.ORB_create()

    # 特徴検出
    keypoints = detector.detect(img)

    # 画像への特徴点の書き込み
    out = cv2.drawKeypoints(img, keypoints, None)

    # 表示
    cv2.imwrite("result3.jpg",out)
    cv2.imshow("keypoints", out)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def HOG():
    converter = cv2.HOGDescriptor()
    img = cv2.imread('img1.jpg')
    hog = cv2.HOGDescriptor()
    out = hog.compute(img)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    #human()
    matching_featurepoint()
    #show_featurepoint()
    #HOG()