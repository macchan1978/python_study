from __future__ import annotations
from typing import TypeVar, Generic
import tkinter as tk
import cv2
from PIL import Image, ImageTk


T = TypeVar('T', bound=tk.Widget)

def grid(widget: T, column: int = 0, row: int = 0, columnspan: int = 1) -> T:
    widget.grid(column=column, row=row, columnspan=columnspan)
    return widget


#MEMO : TypeVarでgenericsを実現
#MEMO : **kwargsでキーワード引数のpassを実現
def pack(widget: T, **kwargs) -> T:
    widget.pack(**kwargs)
    return widget


def setCanvasImage(src: cv2.Mat, canvas: tk.Canvas) -> ImageTk.PhotoImage:
    """
    def setCanvasImage(src: cv2.Mat, canvas: tk.Canvas) -> ImageTk.PhotoImage:
    """
    img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    imgPil = Image.fromarray(img)
    imgTk = ImageTk.PhotoImage(imgPil)
    canvas.create_image(0, 0, image=imgTk, anchor='nw')
    return imgTk
