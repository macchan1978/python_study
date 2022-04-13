from __future__ import annotations
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt


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
    def __init__(self, paddingX=0, paddingY=0):
        self._images: list[tuple[str, cv2.Mat]] = []
        self._padding = [paddingX, paddingY]
        self._location = [0, 0]

    def append(self, windowName: str, image: cv2.Mat):
        cv2.imshow(windowName, image)
        cv2.moveWindow(windowName, self._location[0], self._location[1])
        for i, p in enumerate(self._padding):
            self._location[i] += p
        print(f'new window Location : {self._location[0]} {self._location[1]}')
        self._images.append((windowName, image))

        pass
    pass


imgUtil = ImageWindowUtil(paddingX=50, paddingY=30)
img = cv2.imread('images/cat_image.jpeg')
print(img.shape)
print(f'dtype : {img.dtype}')
imgUtil.append('cat', img)
eye = img[480:630, 450:630]
imgUtil.append('eye', eye)
img[1000:1150, 1000:1180] = eye
imgUtil.append('test', img)
cv2.waitKey(0)
exit()

# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# claheApply = clahe.apply(img)
# equ = cv2.equalizeHist(img)
# show_images([
#     ('img',img),
#     ('equ',equ),
#     ('clahe',claheApply),
# ])

profile = []
for x in range(300):
    profile.append(img[x, 100])
g = plt.subplot()
g.plot(profile)
cv2.imshow("img", img)
plt.show()
cv2.destroyAllWindows()


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
