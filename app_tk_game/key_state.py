from enum import Enum
from bounding_ball import *


class Direction(Enum):
    UP=1
    RIGHT=2
    DOWN=3
    LEFT=4
    NONE=5

class KeyState:
    def __init__(self, control):
        self.direction:Direction = Direction.NONE
        self.button:bool = False
        self.key=''
        self.bind_key_event(control)
    def bind_key_event(self, control):
        control.bind("<KeyPress>", self.on_press_key)
        control.bind("<KeyRelease>", self.on_release_key)
  

    def on_press_key(self, event):
        key = event.keysym
        self.key=key
        if key == 'space':
            self.button = True
        if key == 'Left':
            self.direction = Direction.LEFT
        elif key == 'Down':
            self.direction = Direction.DOWN
        elif key == 'Right':
            self.direction = Direction.RIGHT
        elif key == 'Up':
            self.direction = Direction.UP

    def on_release_key(self, event):
        self.button=False
        self.direction=Direction.NONE
