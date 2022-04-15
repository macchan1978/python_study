from __future__ import annotations
import tkinter as tk
from tkinter import ttk
import cv2
from common import *


class PyramidTestWindow:
    def __init__(self, parent: tk.Tk):
        self.maxSize = Size(1000, 750)
        self.initialPyrLevel = 6
        self.createUi(parent)
        self.onOpenImageFile()

    def createUi(self, parent):
        win = tk.Toplevel(parent)
        win.title('Pyramid Test Window')

        frames: list[ttk.Frame] = [
            ttk.Frame(win),
            ttk.Frame(win)
        ]
        for frame in frames:
            frame.pack(anchor='nw')
        self.createButtonUi(frames[0])
        self.createImageUi(frames[1])

    def createButtonUi(self, frameUpper: tk.Widget):

        uis: list[tk.Widget] = [
            label := ttk.Label(frameUpper, text="Hello World!"),
            ttk.Button(frameUpper, text="inc", command=lambda: self.incPyr()),
            ttk.Button(frameUpper, text="dec", command=lambda: self.decPyr()),
            checkBtn := ttk.Checkbutton(
                frameUpper, text='show hint', command=lambda:self.processPyramid()),
            ttk.Label(frameUpper, text="      "),
            ttk.Button(
                frameUpper, text="open", command=lambda: self.onOpenImageFile())
        ]
        for ui in uis:
            ui.pack(side='left')
        self.label = label
        #MEMO : Checkbuttonの初期値は 'alternate' なのでそのキャンセルが必要。
        checkBtn.state(['!alternate','selected'])
        self.checkButton = checkBtn

    def createImageUi(self, frameLower: tk.Widget):
        def factory(): return CanvasWithImage(tk.Canvas(
            master=frameLower, bg="White", highlightthickness=0))
        canvases: list[CanvasWithImage] = [
            factory(),
            factory()
        ]
        for c in canvases:
            c.canvas.pack(side='left')
        self.canvasPyrUp = canvases[0]
        self.canvasPyrDown = canvases[1]

    def openImageFile(self, filePath: str):
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

    def onOpenImageFile(self):
        filePath = askImageFile()
        if filePath is None:
            return
        self.openImageFile(filePath)

    def processPyramid(self):
        self.label['text'] = f'Pyramid level : {self.pyrLevel}'
        if(self.pyrLevel < 0):
            return
        pyrImage = self.image.copy()
        for i in range(self.pyrLevel):
            pyrImage = cv2.pyrDown(pyrImage)
        self.canvasPyrDown.setImage(pyrImage)
        if self.checkButton.instate(['selected']):
            #TODO : pack()し直しのときにキーワード引数を再度設定するのがスマートではない。hide,showのユーティリティクラスが欲しい。
            self.canvasPyrDown.canvas.pack(side='left')
        else:
            self.canvasPyrDown.canvas.pack_forget()

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
