from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from common import *





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

