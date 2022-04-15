from __future__ import annotations
import random
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

from app_cv_test.common import *


def show_image(title, img, destroy_all=True):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    if(destroy_all):
        cv2.destroyAllWindows()


def show_images(images: list[tuple[str, cv2.Mat]], destroy_all=True):
    for img in images:
        cv2.imshow(img[0], img[1])
    cv2.waitKey(0)
    if(destroy_all):
        cv2.destroyAllWindows()


class ImageWindowUtil:
    """
    cv2.Matを整列表示するためのユーティリティ
    """

    def __init__(self, paddingX: int = 0, paddingY: int = 0, autoPadding: bool = False):
        self._images: list[tuple[str, cv2.Mat]] = []
        self._autoPadding = autoPadding
        self._padding = [paddingX, paddingY]

    def append(self, windowName: str, image: cv2.Mat) -> None:
        cv2.imshow(windowName, image)
        #cv2.moveWindow(windowName, self._location[0], self._location[1])
        self._images.append((windowName, image))

        divNum = len(self._images) if self._autoPadding else 1
        padding = [p//divNum for p in self._padding]
        for i, img in enumerate(self._images):
            x = padding[0]*i
            y = padding[1]*i
            cv2.moveWindow(img[0], x, y)


def thresholdTest():
    imgUtil = ImageWindowUtil(paddingX=50, paddingY=30)
    filePath = askImageFile()
    if not filePath:return
    img = cv2.imread(
        filePath,
        cv2.IMREAD_GRAYSCALE)
    imgUtil.append('original', img)
    ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    imgUtil.append('basic', th1)
    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    imgUtil.append('otsu', th2)
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3, th3 = cv2.threshold(blur, 0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    imgUtil.append('otsu with gaussian', th3)
    cv2.waitKey(0)

    exit()


thresholdTest()


def rotationTest():
    imgUtil = ImageWindowUtil(paddingX=50, paddingY=30)
    image = cv2.imread(askImageFile())
    imgUtil.append('original', image)
    rows, cols, _ = image.shape
    for angle in range(0, 90, 5):
        rot = cv2.getRotationMatrix2D((cols/2.0, rows/2.0), angle, 1)
        rotated = cv2.warpAffine(image, rot, (cols, rows))
        imgUtil.append(f'rotation {angle}', rotated)
    cv2.waitKey(0)
    exit()


def catEyeTest():
    def copyPasteImage(src: cv2.Mat, dst: cv2.Mat, x: int, y: int):
        rows, cols, _ = src.shape
        dst[y:y+rows, x:x+cols] = src
        pass
    imgUtil = ImageWindowUtil(paddingX=50, paddingY=30)
    img = cv2.imread('images/cat_image.jpeg')
    print(img.shape)
    print(f'dtype : {img.dtype}')
    imgUtil.append('cat', img)
    eye = img[480:630, 450:630].copy()
    imgUtil.append('eye', eye)
    for i in range(43):
        x, y = random.randint(1, 1000), random.randint(1, 1000)
        copyPasteImage(eye, img, x, y)

    imgUtil.append('test', img)
    cv2.waitKey(0)
    exit()


# -----------------------------------------------------------------------


def binarizeTest():
    img = cv2.imread("images/cat_image.jpeg", 2)  # Color is BGR not RGB
    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    blurred = cv2.GaussianBlur(img, (11, 11), 0)

    equ = cv2.equalizeHist(img)
    plt.hist(equ.flat, bins=100, range=(0, 100))
    plt.show()
    show_image("img", img)
    show_image("eqHist", equ)
    show_image("blurred", blurred)
    show_image("threshold", th2)


# binarizeTest()


def pyrDownUpTest():
    img = cv2.imread("images/cat_image.jpeg", 1)  # Color is BGR not RGB
    print(img.shape)  # (586, 415, 3)

    pyrNum = 4
    for level in range(pyrNum):
        img = cv2.pyrDown(img)
        cv2.imshow("cat pic resized %d" % level, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    for level in range(pyrNum):
        img = cv2.pyrUp(img)
        cv2.imshow("cat pic resized %d" % level, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    cv2.destroyAllWindows()
