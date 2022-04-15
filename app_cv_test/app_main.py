from __future__ import annotations
import tkinter as tk
from tkinter import ttk
import cv2

from common import *
from tests import *


class CvApp():
    def __init__(self):
        self.mainWindow = tk.Tk()
        ttk.Button(self.mainWindow, text="channel test",
                   command=lambda: self.channelTest()).pack(fill="both")
        ttk.Button(self.mainWindow, text="pyramid",
                   command=lambda: self.pyramidTest()).pack(fill="both")
        ttk.Button(self.mainWindow, text="layout",
                   command=lambda: self.layoutTest()).pack(fill="both")
        ttk.Button(self.mainWindow, text="HSV",
                   command=lambda: self.hsvTest()).pack(fill="both")
        self.windows = []
        self.mainWindow.mainloop()

    def pyramidTest(self):
        self.windows.append(PyramidTestWindow(self.mainWindow))

    def channelTest(self):
        #img = cv2.imread('app_cv_test/images/cat_image.jpg')
        img = cv2.imread('app_cv_test/images/soccer.jpg')
        b, g, r = cv2.split(img)
        imgRbSwap = cv2.merge((r, g, b))

        self.windows.append(ImageWindow(
            self.mainWindow, img, "original_image"))
        self.windows.append(ImageWindow(
            self.mainWindow, imgRbSwap, "red_blue_swap_image"))

    def layoutTest(self):
        self.windows.append(LayoutTestWindow(self.mainWindow))

    def hsvTest(self):
        self.windows.append(ColorSpaceTestWindow(self.mainWindow))


app = CvApp()
