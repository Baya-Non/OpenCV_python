import cv2
import os

if __name__ == '__main__':
    # 定数定義
    ESC_KEY = 27     # Escキー
    S_KEY = 97      # Sキー
    INTERVAL= 33     # 待ち時間
    FRAME_RATE = 30  # fps

    ORG_WINDOW_NAME = "org"
    GAUSSIAN_WINDOW_NAME = "gaussian"

    DEVICE_ID = 0

    savefilename=""

    # 出力先ファイル名
    output_path = "./data/"
    filename = "img"
    png = ".jpg"
    if os.path.exists(output_path):
        pass
    else:
        os.mkdir(output_path)

    # 分類器の指定
    cascade_face_file = "haarcascade_frontalface_alt2.xml"
    cascade_mouth_file = ""
    cascade_eye_file = ""
    cascade = cv2.CascadeClassifier(cascade_face_file)

    # カメラ映像取得
    cap = cv2.VideoCapture(DEVICE_ID)

    # 初期フレームの読込
    end_flag, c_frame = cap.read()
    height, width, channels = c_frame.shape

    # ウィンドウの準備
    cv2.namedWindow(ORG_WINDOW_NAME)
    cv2.namedWindow(GAUSSIAN_WINDOW_NAME)

    sift = cv2.xfeatures2d.SIFT_create()
    i = 0
    # 変換処理ループ
    while end_flag == True:

        # 画像の取得と顔の検出
        img = c_frame
        
        # フレーム表示
        cv2.imshow(ORG_WINDOW_NAME, c_frame)

        # Escキーで終了
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break
        elif key == S_KEY:
            savefilename = output_path + filename + str(i) + png
            print(savefilename)
            cv2.imwrite(savefilename, c_frame)
            i = i+1

        # 次のフレーム読み込み
        end_flag, c_frame = cap.read()

    # 終了処理
    cv2.destroyAllWindows()
    cap.release()