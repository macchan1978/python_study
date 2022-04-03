import tkinter as tk
import random
from bounding_ball import *
from player import *


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
                self.create_circle_shape(b.x, b.y),
                width=2.0,
                outline='#00FF00')

    def create_circle_shape(self, x, y):
        radius = 20
        return (x-radius, y-radius, x+radius, y+radius)
