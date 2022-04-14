from __future__ import annotations
import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk


class Point2i:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class Piont2f:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y


class Size:
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height


def createImageForCanvas(src: cv2.Mat, canvas=None):
    img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    imgPil = Image.fromarray(img)
    imgTk = ImageTk.PhotoImage(imgPil)
    if(not canvas is None):
        canvas.create_image(0, 0, image=imgTk, anchor='nw')
    # MEMO : PhotoImageはGCされないようにfieldで保持する必要がある
    return imgTk


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


class PyramidTestWindow:
    def __init__(self, parent):
        self.size = size = Size(600, 400)
        self.pyrLevel = 6
        self._windows = win = tk.Toplevel(parent)
        win.title('Pyramid Test Window')
        frm = ttk.Frame(win, padding=10)
        frm.grid()
        self.label = label = ttk.Label(frm, text="Hello World!")
        label.grid(column=0, row=0)
        incBtn = ttk.Button(frm, text="inc")
        incBtn.grid(column=1, row=0)
        incBtn.bind("<ButtonPress>", self.incPyr)
        decBtn = ttk.Button(frm, text="dec")
        decBtn.grid(column=2, row=0)
        decBtn.bind("<ButtonPress>", self.decPyr)
        self.canvas = canvas = tk.Canvas(
            frm, width=size.width, height=size.height, bg="White")
        canvas.grid(column=0, row=1, columnspan=3)
        self.canvas2 = canvas2 = tk.Canvas(
            frm, width=size.width, height=size.height, bg="White")
        canvas2.grid(column=0, row=2, columnspan=3)

        # TODO : 画像パスのユーティリティ化
        img = cv2.imread('app_cv_test/images/soccer.jpg')
        #img = cv2.imread('app_cv_test/images/cat_image.jpg')
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

# TODO : なんだか公式ではttkが勧められている?
# https://docs.python.org/3/library/tkinter.ttk.html#using-ttk


class CvApp():
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry('500x100')
        self.button = tk.Button(self.mainWindow, text="channel test")
        self.button.pack()
        self.buttonPyr = tk.Button(self.mainWindow, text="pyramid")
        self.buttonPyr.pack()
        self.button.bind("<ButtonPress>", self.channelTest)
        self.buttonPyr.bind("<ButtonPress>", self.pyramidTest)
        self.windows = []

        pass

    def pyramidTest(self, event):
        self.windows.append(PyramidTestWindow(self.mainWindow))

        pass

    def channelTest(self, event):
        img = cv2.imread('app_cv_test/images/soccer.jpg')
        b, g, r = cv2.split(img)
        imgRbSwap = cv2.merge((r, g, b))

        self.windows.append(ImageWindow(
            self.mainWindow, img, "original_image"))
        self.windows.append(ImageWindow(
            self.mainWindow, imgRbSwap, "red_blue_swap_image"))
        pass

    def run(self):

        self.mainWindow.mainloop()

        pass


app = CvApp()
app.run()
