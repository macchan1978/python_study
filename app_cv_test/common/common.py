from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from typing import Optional
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


class CanvasWithImage:
    """
    tk.Canvasにセットするimageは誰かが保持しないと破棄されてしまう。
    それを防ぐために画像をCanvasとペアで保持するためのユーティリティクラス。
    """

    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas

    def setImage(self, image: cv2.Mat) -> None:
        self.canvas["width"] = image.shape[1]
        self.canvas["height"] = image.shape[0]
        self.imageHolder = fluent.setCanvasImage(image, self.canvas)


class ImageWindow:
    def __init__(self, parent: tk.Tk, image: cv2.Mat, title: str = 'New Window'):
        window = tk.Toplevel(parent)
        window.title(title)

        # MEMO : highlightthicknessを0にしないと(0,0)から有効に使えない
        self.canvas = CanvasWithImage(tk.Canvas(window, highlightthickness=0))
        self.canvas.canvas.pack()
        self.canvas.setImage(image)


def askImageFile() -> Optional[str]:
    result = filedialog.askopenfile(
        initialfile='/Users/shingo/dev/python/python_study/app_cv_test/images/soccer.jpg',
        filetypes=[("Image file", ".jpg .png .tiff .tif")],
        initialdir='/Users/shingo/dev/python/python_study/app_cv_test/images')
    return None if result is None else result.name
