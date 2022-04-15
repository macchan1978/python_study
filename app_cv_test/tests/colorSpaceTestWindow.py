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

        buttonUi = fluent.pack(ttk.Frame(win), anchor='w')
        self.createButtonUi(buttonUi)

        imageUi = fluent.pack(ttk.Frame(win))
        self.canvas = fluent.pack(
            tk.Canvas(imageUi, width=300, height=200, bg='white'))

    def createButtonUi(self, buttonUi):
        # MEMO : **演算子を使うことで複数箇所に設定するキーワード引数をDRY化できる。
        opts = {'side': 'left'}
        fluent.pack(ttk.Button(
            buttonUi,
            text='open', command=lambda: self.openFile()),
            **opts)
        self.textBoxColor = fluent.pack(ttk.Entry(
            buttonUi,
            width=10),
            **opts)
        self.textBoxColor.insert(tk.END, '120')
        self.textBoxColorRange = fluent.pack(ttk.Entry(
            buttonUi,
            width=10),
            **opts)
        self.textBoxColorRange.insert(tk.END, '10')
        fluent.pack(ttk.Button(
            buttonUi,
            text='apply', command=lambda: self.apply()),
            **opts)

    def openFile(self):
        print('openfile')
        result = filedialog.askopenfile(
            initialfile='/Users/shingo/dev/python/python_study/app_cv_test/images/soccer.jpg',
            filetypes=[("Image file", ".jpg .png .tiff .tif")],
            initialdir='/Users/shingo/dev/python/python_study/app_cv_test/images')
        if result is None:
            return
        self.image = cv2.imread(result.name)
        self.processImage()

        pass

    def processImage(self):
        image = self.image.copy()
        # Convert BGR to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        color = int(self.textBoxColor.get())
        colorRange = int(self.textBoxColorRange.get())

        # define range of blue color in HSV
        lower_blue = np.array([color-colorRange, 50, 50])
        upper_blue = np.array([color+colorRange, 255, 255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(image, image, mask=mask)

        self.canvas["width"] = image.shape[1]
        self.canvas["height"] = image.shape[0]
        self.canvasImage = fluent.setCanvasImage(res, self.canvas)

    def apply(self):
        self.processImage()
        pass

    pass
