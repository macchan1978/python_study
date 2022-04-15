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
        self.createImageUi(imageUi)

    def createImageUi(self, imageUi):
        self.canvasOriginal = CanvasWithImage(tk.Canvas(
            imageUi, width=300, height=200, bg='white'))
        self.canvasOriginal.canvas.pack(side='left')

        self.canvasProcessed = CanvasWithImage(tk.Canvas(
            imageUi, width=300, height=200, bg='white'))
        self.canvasProcessed.canvas.pack(side='left')

    def createButtonUi(self, buttonUi):
        # MEMO : **演算子を使うことで複数箇所に設定するキーワード引数をDRY化できる。
        opts = {'side': 'left'}

        openButton = ttk.Button(
            buttonUi, text='open', command=lambda: self.openFile())
        openButton.pack(**opts)

        self.textBoxColor = ttk.Entry(buttonUi, width=10)
        self.textBoxColor.pack(**opts)
        self.textBoxColor.insert(tk.END, '120')

        self.textBoxColorRange = ttk.Entry(buttonUi, width=10)
        self.textBoxColorRange.pack(**opts)
        self.textBoxColorRange.insert(tk.END, '10')

        applyButton = ttk.Button(
            buttonUi, text='apply', command=lambda: self.apply()
        )
        applyButton.pack(**opts)

    def openFile(self):
        filePath = askImageFile()
        if filePath is None:
            return
        self.image = cv2.imread(filePath)
        self.canvasOriginal.setImage(self.image)
        self.processImage()

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

        self.canvasProcessed.setImage(res)

    def apply(self):
        self.processImage()
        pass

    pass
