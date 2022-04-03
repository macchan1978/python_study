import tkinter as tk
from bounding_ball import *
from player import *
from ball_manager import BallManager

class GraphicsApp(tk.Frame):
    def __init__(self, master=None):
        canvas_width = 500
        canvas_height = 400
        tk.Frame.__init__(self, master, width=canvas_width,
                          height=canvas_height)
        self.counter = 0
        self.key_state = KeyState(self)
        self.ball_mgr = BallManager(canvas_width, canvas_height)

        self.player = Player(50, 50)

        self.canvas = tk.Canvas(self)
        self.canvas.place(x=0, y=0, width=canvas_width, height=canvas_height)

        self.focus_set()
        self.update_clock()

    def run(self):
        self.pack()
        self.mainloop()
        #self.update_clock()

    def update_clock(self):
        self.after(20, self.update_clock)
        self.counter += 1
        self.player.tick(self.key_state, self.ball_mgr)
        self.ball_mgr.tick()
        self.on_draw()

    def on_draw(self):
        self.canvas.delete('all')

        # ラインの描画
        # self.c.create_line(10, 30, 230, 30, width=2.0, fill='#FF0000')

        # 円の描画
        self.draw_player()
        self.ball_mgr.draw(self.canvas)

        # 円の塗り潰し
        # self.c.create_oval(70, 70, 110, 110, width=0.0, fill='#00FF00')

        # 矩形の描画
        # self.c.create_rectangle(10, 130, 50, 170, width=2.0, outline='#00A0FF')

        # 矩形の塗り潰し
        # self.c.create_rectangle(70, 130, 110, 170, width=0.0, fill='#00A0FF')

        # 文字列の表示
        self.canvas.create_text(10, 10, text='Hello World %d [%s]' % (
            self.counter, self.key_state.key), font='courier 20', anchor=tk.NW)


    def draw_player(self):
        p = self.player
        self.canvas.create_oval(self.create_circle_shape(
            p.x, p.y), width=0.0, fill='#5555FF')

    def create_circle_shape(self, x, y):
        radius = 20
        return (x-radius, y-radius, x+radius, y+radius)
