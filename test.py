import matplotlib.pyplot as plt
import numpy as np
import math

na = np.array(list(range(100)))
print(na[na%5==0])


def create_bounce_array():
    y=[0]
    v = 10
    a=-0.1
    for i in range(1000):
        v+=a
        nextY = y[-1]+v
        if(nextY<0):
            v=-v*0.8
            nextY=0
        y.append(y[-1]+v)
    return np.array(y)

def create_wave_array():
    y=[]
    stepNum=1000
    for x in range(stepNum):
        rad = math.pi*x/stepNum
        y.append(math.sin(rad*10) + 0.7*math.sin(rad*80))
    return y

def test_wave_array():
    y=create_wave_array()
    g=plt.subplot()
    g.plot(y)
    plt.show()

test_wave_array()

def create_circle_array():
    x=[]
    y=[]
    radius=10
    for rad in np.linspace(0,math.pi*2,100):
        x.append(math.cos(rad)*radius)
        y.append(math.sin(rad)*radius)
    return (np.array(x),np.array(y))

def test_circle():
    circle = create_circle_array()
    g = plt.subplot()
    g.plot(circle[0],circle[1])
    g.set_aspect('equal')
    plt.show()

#test_circle()


def test_bounce():
    y = create_bounce_array()
    plt.plot(y)
    plt.show()    



