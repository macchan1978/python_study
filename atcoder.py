import numpy as np
import math


def f():
    x1, y1, x2, y2 = map(int, input().split())
    c1 = create_candidates(x1, y1)
    c2 = create_candidates(x2, y2)

    interNum = len(c1.intersection(c2))
    print("Yes" if interNum > 0 else "No")


def create_candidates(x, y):
    offsets = [
        (-2, -1),
        (-1, -2),
        (+2, -1),
        (+1, -2),
        (-2, +1),
        (-1, +2),
        (+2, +1),
        (+1, +2),
    ]
    return set([(x+ofs[0], y+ofs[1]) for ofs in offsets])



f()
