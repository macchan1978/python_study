from __future__ import annotations

import tkinter as tk
import cv2
from PIL import Image, ImageTk



# gridをfluentに使えるユーティリティ
def grid(widget: tk.Widget, column: int = 0, row: int = 0, columnspan: int = 1):
    widget.grid(column=column, row=row, columnspan=columnspan)
    return widget


def setCanvasImage(src: cv2.Mat, canvas):
    img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    imgPil = Image.fromarray(img)
    imgTk = ImageTk.PhotoImage(imgPil)
    canvas.create_image(0, 0, image=imgTk, anchor='nw')
    return imgTk

