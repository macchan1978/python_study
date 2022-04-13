import tkinter as tk
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


class ImageWindow():
    def __init__(self, parent:tk.Tk, width=100, height=100):
        self.width = width
        self.height = height
        self._window = tk.Toplevel(parent)
        self._window.title("New Window")
        self._window.geometry(f'{width}x{height}')
        self._canvas = tk.Canvas(self._window, highlightthickness=0)
        self._canvas.place(x=0, y=0, width=width, height=height)
        self.onDraw()

    def onDraw(self):
        self._canvas.delete('all')
        self._canvas.create_text(0,0,text="hello,world",anchor='nw')

        img_ = cv2.imread('app_cv_test/images/cat_image.jpeg')
        img = cv2.resize(img_, dsize=(self.width, self.height))
        #img = cv2.resize(img_,dsize=(200,200))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgPil = Image.fromarray(img)
        self.imgTk = ImageTk.PhotoImage(imgPil)
        self._canvas.create_image(0, 0, image=self.imgTk, anchor='nw')

        pass


class CvApp():
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry('500x100')
        self.button = tk.Button(self.mainWindow,text="start")
        self.button.pack()
        self.button.bind("<ButtonPress>",self.buttonClick)

        pass

    def buttonClick(self, event):
        self.child = ImageWindow(self.mainWindow, 600, 600)
        pass
    def run(self):

        self.mainWindow.mainloop()

        pass


app = CvApp()
app.run()
