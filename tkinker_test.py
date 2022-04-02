import math
import random
import tkinter as tk
from tkinter import messagebox

class PackApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('ウィジェットの一列配置')
        self.master.geometry('240x240')

        label1 = tk.Label(self, text='label1', bg='red')
        label1.pack(padx=5, pady=5)

        label2 = tk.Label(self, text="label2",bg='green')
        label2.pack(padx=5, pady=5)

        label3 = tk.Label(self, text="label3",bg='blue')
        label3.pack(padx=5, pady=5)


class GridApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)

        self.master.title('grid of widgets')
        self.master.geometry('240x240')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        label1=tk.Label(self,text='label1', bg='red', height=100)
        label1.grid(row=0,column=0,columnspan=2,sticky='news',padx=5,pady=5)
        
        label2=tk.Label(self,text='label2', bg='green')
        label2.grid(row=1,column=0,sticky='news',padx=5,pady=5)

        label3=tk.Label(self,text='label3', bg='blue')
        label3.grid(row=1,column=1,sticky='news',padx=5,pady=5)


class BoundingBall:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.vx=4
        self.vy=4
        self.width=width
        self.height=height

    def tick(self):
        self.x+=self.vx
        self.y+=self.vy
        self.update_x_bounce()
        self.update_y_bounce()
    
    def update_x_bounce(self):
        if self.x < 0:
            self.vx = abs(self.vx)
        elif self.x >self.width:
            self.vx = -abs(self.vx)

    def update_y_bounce(self):
        if self.y < 0:
            self.vy = abs(self.vy)
        elif self.y >self.height:
            self.vy = -abs(self.vy)


class GraphicsApp(tk.Frame):
    def __init__(self,master=None):
        width=500
        height=400
        tk.Frame.__init__(self,master,width=width, height=height)
        self.counter = 0
        self.is_update=False

        self.balls=[]
        for i in range(100):
            x = random.randint(0,width)
            y= random.randint(0,height)
            self.balls.append(BoundingBall(x,y, width, height))


        self.ball = BoundingBall(10,10,width,height )

        self.c = tk.Canvas(self)
        self.c.place(x=0,y=0, width=width, height=height)

        self.push_button=tk.Button(self, text='push', command=self.on_click)
        self.push_button.place(x=20,y=240,width=100,height=50)

        self.update_clock()

        #self.on_draw()
    
    def on_click(self):
        self.is_update=not self.is_update


    def update_clock(self):
        self.after(20, self.update_clock)
        if not self.is_update:
            return
        self.counter +=1
        self.ball.tick()
        for b in self.balls:
            b.tick()
        self.on_draw() 

    def on_draw(self):
        self.c.delete('all')

        # ラインの描画
        self.c.create_line(10, 30, 230, 30, width=2.0, fill='#FF0000')

        # 円の描画
        self.draw_circle()

        # 円の塗り潰し
        self.c.create_oval(70, 70, 110, 110, width=0.0, fill='#00FF00')

        # 矩形の描画
        self.c.create_rectangle(10, 130, 50, 170, width=2.0, outline='#00A0FF')

        # 矩形の塗り潰し
        self.c.create_rectangle(70, 130, 110, 170, width=0.0, fill='#00A0FF')

        # 文字列の表示
        self.c.create_text(10, 200, text='Hello World %d'%self.counter, font='courier 20', anchor=tk.NW) 

    def draw_circle(self):
        for b in self.balls:
            self.c.create_oval(self.create_circle_shape(b.x, b.y), width=2.0, outline='#00FF00') 


    def create_circle_shape(self, x, y):
        radius=20
        return (x-radius, y-radius, x+radius, y+radius)      



app=GraphicsApp()
app.pack()
app.mainloop()