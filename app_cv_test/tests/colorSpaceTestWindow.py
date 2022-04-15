from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import cv2
from common import *


class ColorSpaceTestWindow:
    def __init__(self, parent: tk.Tk):
        win = tk.Toplevel(parent)
        win.title('Color Space Test Window')

        # ボタンUI部---
        buttonUi = fluent.pack(ttk.Frame(win), anchor='w')
        # MEMO : **演算子を使うことで複数箇所に設定するキーワード引数をDRY化できる。
        opts = {'side': 'left'}
        fluent.pack(ttk.Button(
            buttonUi,
            text='open', command=lambda: self.openFile()),
            **opts)
        self.textBox = fluent.pack(ttk.Entry(
            buttonUi,
            width=10),
            **opts)
        fluent.pack(ttk.Button(
            buttonUi,
            text='apply', command=lambda: self.apply()),
            **opts)

        # 画像表示部---
        imageUi = fluent.pack(ttk.Frame(win))
        self.canvas = fluent.pack(
            tk.Canvas(imageUi, width=300, height=200, bg='white'),
            **opts)

        pass

    def openFile(self):
        print('openfile')
        result = filedialog.askopenfile(
            filetypes=[("Image file", ".jpg .png .tiff .tif")],
            initialdir='/Users/shingo/dev/python/python_study/app_cv_test/images')
        if result is None:
            return
        filePath = result.name

        frame = cv2.imread(filePath)

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)

        self.canvas["width"]=frame.shape[1]
        self.canvas["height"]=frame.shape[0]
        self.canvasImage = fluent.setCanvasImage(res, self.canvas)

        pass

    def apply(self):
        print('apply')
        self.textBox
        pass

    pass
