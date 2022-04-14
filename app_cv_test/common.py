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


def gridCanvas(canvas: tk.Canvas, column: int = 0, row: int = 0, columnspan: int = 1):
    canvas.grid(column=column, row=row, columnspan=columnspan)
    return canvas

