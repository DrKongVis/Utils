import cv2
import numpy as np


# 全局阈值
def threshold_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    print("阈值：", ret)
    cv2.imshow("binary", binary)
    # cv2.imwrite("F:\\Desktop\\Code\\script\\pythonProject\\other\\1.png", binary)
    print("写出完成")


# 局部阈值
def local_threshold(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
    # binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,10)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    cv2.imshow("binary ", binary)


def custom_threshold(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    mean = m.sum()/(w*h)
    # binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,10)
    ret, binary = cv2.threshold(gray, mean, 255, cv2.THRESH_BINARY)
    # cv2.imshow("binary ", binary)


if __name__ == "__main__":
    img = cv2.imread("other/1.jpg")
    cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input image", img)
    threshold_demo(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()