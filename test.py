from __future__ import annotations
import timeit
import matplotlib.pyplot as plt
import numpy as np
import math


time = timeit.timeit('a,b=42,101;a=a^b;b=a^b;a=a^b')
print(f'consumed time 1: {time}')
time = timeit.timeit('a,b=42,101;temp=a;a=b;b=temp')
print(f'consumed time 2: {time}')
time = timeit.timeit('a,b=42,101;a,b=b,a')
print(f'consumed time 3: {time}')


def makeTuple(name: str, age: int) -> tuple[str, int]:
    return (name, age)


def describeNumber(number: int) -> str:
    '''A number describing function.

    Basic Usage::
    resultStr = descriveNumber(1234)
    '''
    print(f'describeNumber : {number}')
    if number % 2 == 1:
        return "this is odd"
    else:
        return "this is even"


def create_bounce_array():
    y = [0.0]
    v = 10
    a = -0.1
    for _ in range(1000):
        v += a
        nextY = y[-1]+v
        if(nextY < 0):
            v = -v*0.8
            nextY = 0
        y.append(y[-1]+v)
    return np.array(y)


def create_wave_array():
    y = []
    stepNum = 1000
    for x in range(stepNum):
        rad = math.pi*x/stepNum
        y.append(math.sin(rad*10) + 0.7*math.sin(rad*80))
    return y


def test_wave_array():
    y = create_wave_array()
    g = plt.subplot()
    g.plot(y)
    plt.show()

# test_wave_array()


def create_circle_array():
    x = []
    y = []
    radius = 10
    for rad in np.linspace(0, math.pi*2, 100):
        x.append(math.cos(rad)*radius)
        y.append(math.sin(rad)*radius)
    return (np.array(x), np.array(y))


def test_circle():
    circle = create_circle_array()
    g = plt.subplot()
    g.plot(circle[0], circle[1])
    g.set_aspect('equal')
    plt.show()

# test_circle()


def test_bounce():
    y = create_bounce_array()
    plt.plot(y)
    plt.show()
