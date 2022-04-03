import tkinter as tk
import random
from bounding_ball import *
from player import *
import tk_shape


class BallManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.balls = []
        for i in range(0):
            x = random.randint(0, width)
            y = random.randint(0, height)
            self.balls.append(BoundingBall(x, y, width, height))

    def tick(self):
        for b in self.balls:
            b.tick()

    def shot(self, x, y):
        self.balls.append(BoundingBall(x, y, self.width, self.height))

    def draw(self, canvas: tk.Canvas):
        for b in self.balls:
            canvas.create_oval(
                tk_shape.create_circle(b.x, b.y, 20),
                width=2.0,
                outline='#00FF00')
