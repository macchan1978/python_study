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
        width = image.shape[1] if width == 0 else width
        height = image.shape[0] if height == 0 else height

        window = tk.Toplevel(parent)
        window.title(title)
        # MEMO : highlightthicknessを0にしないと(0,0)から有効に使えない
        canvas = fluent.pack(
            tk.Canvas(window, highlightthickness=0,
                      width=width, height=height))
        self.imgTk = fluent.setCanvasImage(image, canvas)

        pass

