from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import cv2
from common import *


class PyramidTestWindow:
    def __init__(self, parent: tk.Tk):
        self.maxSize = Size(600, 400)
        self.initialPyrLevel = 6
        self._windows = win = tk.Toplevel(parent)
        win.title('Pyramid Test Window')

        frameUpper = ttk.Frame(win,)
        frameUpper.pack(anchor='nw')
        self.createButtonUi(frameUpper)

        frameLower = ttk.Frame(win)
        frameLower.pack()
        self.createImageUi(frameLower)

        self.onOpenImageFile()


    def openImageFile(self, filePath:str):
        self.pyrLevel = self.initialPyrLevel
        img = cv2.imread(filePath)
        # 適切な縮小比率を計算
        yRatio = self.maxSize.height/img.shape[0]
        xRatio = self.maxSize.height/img.shape[1]
        ratio = min(1, yRatio, xRatio)
        resizedImg = cv2.resize(src=img, dsize=[0, 0], fx=ratio, fy=ratio)

        # cv2.imread('app_cv_test/images/cat_image.jpg')
        self.image = resizedImg
        self.processPyramid()

    def createImageUi(self, frameLower: tk.Widget):
        self.canvasPyrUp = CanvasWithImage(tk.Canvas(
            master=frameLower, bg="White"))
        self.canvasPyrUp.canvas.pack(side='left')

        self.canvasPyrDown = CanvasWithImage(tk.Canvas(
            master=frameLower, bg="White"))
        self.canvasPyrDown.canvas.pack(side='left')

    def createButtonUi(self, frameUpper: tk.Widget):
        sideLeft = {'side': 'left'}
        self.label = label = ttk.Label(frameUpper, text="Hello World!")
        label.pack(**sideLeft)

        ttk.Button(
            frameUpper, text="inc", command=lambda: self.incPyr()
        ).pack(**sideLeft)

        ttk.Button(
            frameUpper, text="dec", command=lambda: self.decPyr()
        ).pack(**sideLeft)

        ttk.Button(
            frameUpper, text="open", command=lambda: self.onOpenImageFile()
        ).pack(**sideLeft)

    def onOpenImageFile(self):
        # TODO : 画像パスのユーティリティ化
        result = filedialog.askopenfile(
            initialfile='/Users/shingo/dev/python/python_study/app_cv_test/images/soccer.jpg',
            filetypes=[("Image file", ".jpg .png .tiff .tif")],
            initialdir='/Users/shingo/dev/python/python_study/app_cv_test/images')
        if result is None:
            return
        self.openImageFile(result.name)

    def processPyramid(self):
        self.label['text'] = f'Pyramid level : {self.pyrLevel}'
        if(self.pyrLevel < 0):
            return
        pyrImage = self.image.copy()
        for i in range(self.pyrLevel):
            pyrImage = cv2.pyrDown(pyrImage)
        self.canvasPyrDown.setImage(pyrImage)

        for i in range(self.pyrLevel):
            pyrImage = cv2.pyrUp(pyrImage)
        self.canvasPyrUp.setImage(pyrImage)

    def incPyr(self):
        self.pyrLevel += 1
        self.processPyramid()
        pass

    def decPyr(self):
        self.pyrLevel -= 1
        self.processPyramid()
        pass

    pass
