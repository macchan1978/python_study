from ball_manager import BallManager
from key_state import *


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tick(self, key: KeyState, ballMgr : BallManager):
        v = 5
        vx, vy = (0, 0)
        if(key.direction == Direction.LEFT):
            vx = -v
        if(key.direction == Direction.RIGHT):
            vx = v
        if(key.direction == Direction.UP):
            vy = -v
        if(key.direction == Direction.DOWN):
            vy = v
        self.x += vx
        self.y += vy
        if(key.button is True):
            ballMgr.shot(self.x, self.y)
            key.button = False
