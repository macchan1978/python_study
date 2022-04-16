from __future__ import annotations
import tkinter as tk
from tkinter import ttk
import cv2
from common import *


class WebCamWindow:
    def __init__(self, parent: tk.Tk):
        win = tk.Toplevel(parent)
        win.title('WebCam Test Window')
        self.root = self.RootWindow(win)

        pass

    class RootWindow:
        def __init__(self, selfUi: tk.Toplevel):
            self.ui = selfUi
            uis = [ttk.Frame(selfUi), ttk.Frame(selfUi)]
            for ui in uis:
                ui.pack(fill='both')
            self.panelUpper = self.PanelUpper(uis[0])
            self.panelLower = self.PanelLower(uis[1])
        pass

        class PanelUpper:
            def __init__(self, selfUi: tk.Widget):
                self.ui = selfUi
                self.infoLabel = ttk.Label(selfUi, text='test')
                self.infoLabel.pack(side='left')
                self.captureButton = ttk.Button(selfUi, text='capture')
                self.captureButton.pack(side='left')

                pass

        class PanelLower:
            def __init__(self, selfUi: tk.Widget):
                self.ui = selfUi
                self.canvas = tk.Canvas(
                    selfUi, width=600, height=400, bg='white', highlightthickness=0)
                self.canvas.pack()
                pass
