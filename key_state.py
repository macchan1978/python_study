from enum import Enum
from bounding_ball import *


class Direction(Enum):
    UP=1
    RIGHT=2
    DOWN=3
    LEFT=4
    NONE=5

class KeyState:
    def __init__(self):
        self.direction:Direction = Direction.NONE
        self.button:bool = False

