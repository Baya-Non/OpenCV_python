import sys
sys.path.append('/usr/local/Cellar/opencv/3.4.1_5/lib/python3.6/site-packages')
import cv2

def main():
    # 画像の読み込み(RGB)
    img = cv2.imread("lena.png")

	# グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # cv2.GaussianBlur
    dst3 = cv2.GaussianBlur(gray, ksize=(3,3), sigmaX=1.3)

    # 画像の読み込み(RGBA)
    rgba = cv2.imread("input.png", -1)

    # 画素値の表示
    print("rgb=", img)
    print("\n------------------------\n")
    print("gray=", gray)
    print("\n------------------------\n")
    print("rgba=", rgba)

    cv2.imwrite("output3.jpg", dst3)

if __name__ == "__main__":
    main()

    