from Tkinter import *
import time
import math
import pygame

# Circle function based on center and radius, because the arguments for creating oval in tkinter is a pain to compute everytime


def create_circle(xm1, ym1, rad):
    canvas.create_oval(xm1-rad, ym1-rad, xm1+rad, ym1+rad, fill="white")



# creating the canvas
tk = Tk()
my_color = '#%02x%02x%02x' % (0, 10, 15)
canvas = Canvas(tk, width=900, height=900, bg=my_color)
tk.title("Double Pendulum")
canvas.pack()

# initializing all variables
a1 = math.pi/2  # angle of the top Pendulum
a2 = math.pi/2  # angle of the bottom pendulum
l1 = 150  # length of pendulum 1
l2 = 150  # length of pendulum 2
g = 10  # universal gravitational constant
m1 = 100  # mass of first Pendulum
m2 = 100  # mass of second Pendulum
px2 = -1  # previous x position of the second pendulum
py2 = -1  # previous y position of the second pendulum
a1_v = 0  # initial velocity of top Pendulum
a2_v = 0  # initial velocity of bottom Pendulum
clock = 0  # update for the loop

while clock < 10000:

    # initializing x,y positions of the pendulums
    x1 = 450 + l1 * math.sin(a1)
    y1 = 200 + l1 * math.cos(a1)
    x2 = x1 + l2 * math.sin(a2)
    y2 = y1 + l2 * math.cos(a2)

    # drawing a line between previous (x,y) of the second pendulum to the current (x,y)
    if px2 != -1:
        ln2 = canvas.create_line(px2, py2, x2, y2, width=3, fill="white")

    # Calulating the monstrous angular acceleration terms for both pendulums
    num1 = g * (2 * m1 + m2) * math.sin(a1)
    num2 = m2 * g * math.sin(a1 - (2 * a2))
    num3 = 2 * math.sin(a1 - a2) * m2
    num4 = float((a2_v * a2_v * l2) + (a1_v * a1_v * l1 * math.cos(a1 - a2)))
    num_fin = -num1 - num2 - (num3 * num4)
    den1 = float(l1 * ((2 * m1) + m2 - (m2 * math.cos(2 * a1 - 2 * a2))))

    a2_num1 = float(2 * math.sin(a1 - a2))
    a2_num2 = float(a1_v * a1_v * l1 * (m1 + m2))
    a2_num3 = float(g * (m1 + m2) * math.cos(a1))
    a2_num4 = float(a2_v * a2_v * l2 * m2 * math.cos(a1 - a2))
    a2_den2 = float(l2 * (2 * m1 + m2 - (m2 * math.cos(2 * a1 - 2 * a2))))
    a2_num_fin = a2_num1 * (a2_num2 + a2_num3 + a2_num4)

    a1_a = num_fin / den1
    a2_a = a2_num_fin / a2_den2

    # updating angular velocity and position based on angular acceleration
    a1_v += a1_a*0.1
    a2_v += a2_a*0.1
    a1 += a1_v*0.1
    a2 += a2_v*0.1

    # recording previous x,y positions to draw segments between (px2, py2) and (x2, y2)
    px1 = x1
    py1 = y1
    px2 = x2
    py2 = y2

    # updating the loop
    clock += 1
    print(a1_a)
    time.sleep(0.0001)
    tk.update()

mainloop()
