from __future__ import annotations
import tkinter as tk
from tkinter import ttk
import cv2
from common import *


class WebCamWindow:
    def __init__(self, parent: tk.Tk):
        self.tk=parent
        self.counter=0
        self.playing=False
        
        win = tk.Toplevel(parent)
        win.title('WebCam Test Window')
        self.root = self.RootWindow(win)

        self.root.panelUpper.playStopButton['command']=lambda:self.playStopMovie()


    def playStopMovie(self):
        if self.playing:
            self.playing=False
            self.tk.after_cancel(self.afterid)
        else:
            self.playing=True
            self.capture = cv2.VideoCapture(0)
            self.captureFrame()
        pass

    def captureFrame(self):
        ref,frame = self.capture.read()
        self.root.panelLower.canvas.setImage(frame)
        self.counter+=1
        self.afterid = self.tk.after(20,self.captureFrame)


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
                self.playStopButton = ttk.Button(selfUi, text='start')
                self.playStopButton.pack(side='left')

                pass

        class PanelLower:
            def __init__(self, selfUi: tk.Widget):
                self.ui = selfUi
                self.canvas = CanvasWithImage(tk.Canvas(
                    selfUi, width=600, height=400, bg='white', highlightthickness=0))
                self.canvas.canvas.pack()
                pass
