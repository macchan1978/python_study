from re import S
import tkinter as tk
import random
from bounding_ball import *
from player import *




class GraphicsApp(tk.Frame):
    def __init__(self,master=None):
        canvas_width=500
        canvas_height=400
        tk.Frame.__init__(self,master,width=canvas_width, height=canvas_height)
        self.counter = 0
        self.is_update=False
        self.key_name=''
        self.key_state=KeyState()

        self.balls=[]
        for i in range(100):
            x = random.randint(0,canvas_width)
            y= random.randint(0,canvas_height)
            self.balls.append(BoundingBall(x,y, canvas_width, canvas_height))
        self.player = Player(50,50)


        self.c = tk.Canvas(self)
        self.c.place(x=0,y=0, width=canvas_width, height=canvas_height)

        self.push_button=tk.Button(self, text='push', command=self.on_click)
        self.push_button.place(x=20,y=240,width=100,height=50)

        self.update_clock()
        self.bind("<KeyPress>", self.on_press_key)
        self.bind("<KeyRelease>", self.on_release_key)
        self.focus_set()

        #self.on_draw()
    
    def on_press_key(self,event):
        self.key_name = event.keysym
        key = event.keysym
        result = KeyState()
        if key == 'space':
            result.button=True
        if key == 'Left':
            result.direction=Direction.LEFT
        elif key == 'Down':
            result.direction=Direction.DOWN
        elif key == 'Right':
            result.direction=Direction.RIGHT
        elif key == 'Up':
            result.direction=Direction.UP
        self.key_state = result

    def on_release_key(self,event):
        self.key_name = event.keysym
        result = KeyState()
        self.key_state = result


    def run(self):
        self.pack()
        self.mainloop()

    def on_click(self):
        self.is_update=not self.is_update


    def update_clock(self):
        self.after(20, self.update_clock)
        if not self.is_update:
            return
        self.counter +=1
        self.player.tick(self.key_state)
        for b in self.balls:
            b.tick()
        self.on_draw() 

    def on_draw(self):
        self.c.delete('all')

        # ラインの描画
        #self.c.create_line(10, 30, 230, 30, width=2.0, fill='#FF0000')

        # 円の描画
        self.draw_circle()
        self.draw_player()

        # 円の塗り潰し
        #self.c.create_oval(70, 70, 110, 110, width=0.0, fill='#00FF00')

        # 矩形の描画
        #self.c.create_rectangle(10, 130, 50, 170, width=2.0, outline='#00A0FF')

        # 矩形の塗り潰し
        #self.c.create_rectangle(70, 130, 110, 170, width=0.0, fill='#00A0FF')

        # 文字列の表示
        self.c.create_text(10, 200, text='Hello World %d [%s]'%(self.counter,self.key_name), font='courier 20', anchor=tk.NW) 

    def draw_circle(self):
        for b in self.balls:
            self.c.create_oval(self.create_circle_shape(b.x, b.y), width=2.0, outline='#00FF00') 
    def draw_player(self):
        p = self.player
        self.c.create_oval(self.create_circle_shape(p.x, p.y),width=0.0, fill='#5555FF')


    def create_circle_shape(self, x, y):
        radius=20
        return (x-radius, y-radius, x+radius, y+radius)      
