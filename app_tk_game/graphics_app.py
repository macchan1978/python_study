import tkinter as tk
from field import Field
from key_state import KeyState
from player import Player
from ball_manager import BallManager


class GraphicsApp(tk.Frame):
    def __init__(self, master=None):
        self.field = Field(500, 400)
        tk.Frame.__init__(self, master,
                          width=self.field.width,
                          height=self.field.height)
        self.canvas = tk.Canvas(self)
        self.canvas.place(x=0, y=0, width=self.field.width, height=self.field.height)

        self.counter = 0
        self.key_state = KeyState(self)
        self.ball_mgr = BallManager(self.field)

        self.player = Player(50, 50)


        self.focus_set()
        self.update_clock()


    def run(self):
        self.pack()
        self.mainloop()
        # なぜかここで呼ぶと例外が出る
        # self.update_clock()

    def update_clock(self):
        self.after(20, self.update_clock)
        self.counter += 1
        self.player.tick(self.key_state, self.ball_mgr)
        self.ball_mgr.tick()
        self.on_draw()

    def on_draw(self):
        self.canvas.delete('all')
        self.player.draw(self.canvas)
        self.ball_mgr.draw(self.canvas)
        # self.c.create_line(10, 30, 230, 30, width=2.0, fill='#FF0000')
        # self.c.create_rectangle(10, 130, 50, 170, width=2.0, outline='#00A0FF')
        self.canvas.create_text(10, 10, text='Hello World %d [%s]' % (
            self.counter, self.key_state.key), font='courier 20', anchor=tk.NW)
