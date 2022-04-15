from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from typing import Callable
import cv2

from common import *
from tests import *


class CvApp():
    def __init__(self):
        self.mainWindow = tk.Tk()

        def buttonFactory(text: str, command: Callable[[], None]): return ttk.Button(
            self.mainWindow, text=text, command=command)
        uis: list[tk.Widget] = [
            buttonFactory("channel test", lambda:self.channelTest()),
            buttonFactory("pyramid", lambda:self.pyramidTest()),
            buttonFactory("HSV", lambda:self.hsvTest()),
        ]
        for ui in uis:
            ui.pack(fill='both')

        self.windows = []
        self.mainWindow.mainloop()

    def pyramidTest(self):
        self.windows.append(PyramidTestWindow(self.mainWindow))

    def channelTest(self):
        filePath = askImageFile()
        if filePath is None:
            return
        img = cv2.imread(filePath)
        b, g, r = cv2.split(img)
        imgRbSwap = cv2.merge((r, g, b))

        self.windows.append(ImageWindow(
            self.mainWindow, img, "original_image"))
        self.windows.append(ImageWindow(
            self.mainWindow, imgRbSwap, "red_blue_swap_image"))

    def hsvTest(self):
        self.windows.append(ColorSpaceTestWindow(self.mainWindow))


app = CvApp()
