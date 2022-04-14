from __future__ import annotations
import tkinter as tk
from tkinter import ttk
import cv2
from tests.pyramidTestWindow import PyramidTestWindow
from common import *



class ImageWindow:
    def __init__(self, parent: tk.Tk, image: cv2.Mat, title: str = 'New Window', width: int = 0, height: int = 0):
        self.size = Size(
            width if width != 0 else image.shape[1],
            height if height != 0 else image.shape[0])
        self._window = tk.Toplevel(parent)
        self._window.title(title)
        self._window.geometry(f'{self.size.width}x{self.size.height}')
        # MEMO : highlightthicknessを0にしないと(0,0)から有効に使えない
        self._canvas = tk.Canvas(self._window, highlightthickness=0)
        self._canvas.place(x=0, y=0,
                           width=self.size.width,
                           height=self.size.height)
        self.draw(image)

    def draw(self, image: cv2.Mat):
        self._canvas.delete('all')
        self._canvas.create_text(0, 0, text="hello,world", anchor='nw')
        self.imgTk = createImageForCanvas(image, self._canvas)

        pass




# TODO : なんだか公式ではttkが勧められている?
# https://docs.python.org/3/library/tkinter.ttk.html#using-ttk


class LayoutTestWindow:
    def __init__(self, parent: tk.Tk):
        self.window = window = tk.Toplevel(parent)
        window.grid()

        self.frameLeftTop = frameLeftTop = ttk.Frame(window)
        frameLeftTop.grid(column=0, row=0)
        ttk.Button(frameLeftTop, text="label1",).pack()

        self.frameRightTop = frameRightTop = ttk.Frame(window)
        frameRightTop.grid(column=1, row=0)
        ttk.Button(frameRightTop, text="label2").pack()

        self.frameBottom = frameBottom = ttk.Frame(window)
        frameBottom.grid(column=0, columnspan=2, row=1)
        ttk.Button(frameBottom, text="label3").pack()

        pass
    pass


class CvApp():
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry('500x100')
        ttk.Button(self.mainWindow, text="channel test",
                  command=lambda: self.channelTest()).pack()
        ttk.Button(self.mainWindow, text="pyramid",
                  command=lambda: self.pyramidTest()).pack()
        ttk.Button(self.mainWindow, text="layout",
                  command=lambda: self.layoutTest()).pack()
        self.windows = []

    def pyramidTest(self):
        self.windows.append(PyramidTestWindow(self.mainWindow))

    def channelTest(self):
        img = cv2.imread('app_cv_test/images/soccer.jpg')
        b, g, r = cv2.split(img)
        imgRbSwap = cv2.merge((r, g, b))

        self.windows.append(ImageWindow(
            self.mainWindow, img, "original_image"))
        self.windows.append(ImageWindow(
            self.mainWindow, imgRbSwap, "red_blue_swap_image"))

    def layoutTest(self):
        self.windows.append(LayoutTestWindow(self.mainWindow))

    def run(self):

        self.mainWindow.mainloop()

        pass


app = CvApp()
app.run()
