from __future__ import annotations
import tkinter as tk
from tkinter import ttk
import cv2
from common import *





class PyramidTestWindow:
    def __init__(self, parent: tk.Tk):
        self.size = size = Size(600, 400)
        self.pyrLevel = 6
        self._windows = win = tk.Toplevel(parent)
        win.title('Pyramid Test Window')

        # 解像度変更UI
        frameUpper = ttk.Frame(win)
        frameUpper.pack(anchor='ne')

        self.label = label = ttk.Label(frameUpper, text="Hello World!")
        label.grid(column=0, row=0)

        ttk.Button(frameUpper, text="inc",
                   command=lambda: self.incPyr(None)
                   ).grid(column=1, row=0)

        ttk.Button(frameUpper, text="dec",
                   command=lambda: self.decPyr(None)
                   ).grid(column=2, row=0)

        # 2枚の画像を表示するUI
        frameLower = ttk.Frame(win)
        frameLower.pack()
        self.canvas = gridCanvas(tk.Canvas(
            master=frameLower, width=size.width, height=size.height, bg="White"),
            column=0, row=0)

        self.canvas2 = gridCanvas(tk.Canvas(
            master=frameLower, width=size.width, height=size.height, bg="White"),
            column=1, row=0)

        # TODO : 画像パスのユーティリティ化
        #img = cv2.imread('app_cv_test/images/soccer.jpg')
        img = cv2.imread('app_cv_test/images/cat_image.jpg')
        # 適切な縮小比率を計算
        yRatio = size.height/img.shape[0]
        xRatio = size.height/img.shape[1]
        ratio = min(1, yRatio, xRatio)
        resizedImg = cv2.resize(src=img, dsize=[0, 0], fx=ratio, fy=ratio)

        # cv2.imread('app_cv_test/images/cat_image.jpg')
        self.image = resizedImg
        self.updatePyrLevelStr()

    def updatePyrLevelStr(self):
        self.label['text'] = f'Pyramid level : {self.pyrLevel}'
        if(self.pyrLevel < 0):
            return
        pyrImage = self.image.copy()
        for i in range(self.pyrLevel):
            pyrImage = cv2.pyrDown(pyrImage)
        self.tkImage = createImageForCanvas(pyrImage, self.canvas)
        for i in range(self.pyrLevel):
            pyrImage = cv2.pyrUp(pyrImage)
        self.tkImage2 = createImageForCanvas(pyrImage, self.canvas2)

    def incPyr(self, event):
        self.pyrLevel += 1
        self.updatePyrLevelStr()
        pass

    def decPyr(self, event):
        self.pyrLevel -= 1
        self.updatePyrLevelStr()
        pass

    pass