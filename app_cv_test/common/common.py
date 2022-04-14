from __future__ import annotations
import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

from . import fluent



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
        self.imgTk = fluent.setCanvasImage(image, self._canvas)
        #self.imgTk = createImageForCanvas(image, self._canvas)

        pass


# def createImageForCanvas(src: cv2.Mat, canvas=None):
#     img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
#     imgPil = Image.fromarray(img)
#     imgTk = ImageTk.PhotoImage(imgPil)
#     if(not canvas is None):
#         canvas.create_image(0, 0, image=imgTk, anchor='nw')
#     # MEMO : PhotoImageはGCされないようにfieldで保持する必要がある
#     return imgTk


# # gridをfluentに使えるユーティリティ
# def gridCanvas(canvas: tk.Widget, column: int = 0, row: int = 0, columnspan: int = 1):
#     canvas.grid(column=column, row=row, columnspan=columnspan)
#     return canvas

