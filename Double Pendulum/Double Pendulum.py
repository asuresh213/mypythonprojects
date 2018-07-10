from Tkinter import *
import time
import math
import pygame


def create_circle(xm1, ym1, rad):
    canvas.create_oval(xm1-rad, ym1-rad, xm1+rad, ym1+rad, fill="white")


clock = 0


tk = Tk()
my_color = '#%02x%02x%02x' % (0, 10, 15)
canvas = Canvas(tk, width=900, height=900, bg=my_color)
tk.title("Double Pendulum")
canvas.pack()
a1 = math.pi/2
a2 = math.pi/2
l1 = 150
l2 = 150
g = 10
m1 = 100
m2 = 100


# x1 = 450 + l1*math.sin(a1)
# y1 = 200 + l1*math.cos(a1)
# x2 = x1 + l2*math.sin(a2)
# y2 = y1 + l2*math.cos(a2)


# g = 10
# canvas.create_line(300, 100, x1, y1, fill="white", width=2)
# bob1 = create_circle(x1, y1, 2)
# canvas.create_line(x1, y1, x2, y2, fill="white", width=2)
# bob2 = create_circle(x2, y2, 2)

# px1 = 450 + l1 * math.sin(a1)
px2 = -1
# py1 = x1 + l2 * math.sin(a2)
py2 = -1


a1_v = 0
a2_v = 0
update = 0
while clock < 10000:
    # bob1 = create_circle(x1, y1, 1)
    # bob2 = create_circle(x2, y2, 1)
    # x1_v = a1_v * (l1 * math.cos(a1))
    # x2_v = x1_v + a2_v * (l2 * math.cos(a2))
    # y1_v = a1_v * (l1 * math.sin(a1))
    # y2_v = y1_v + a2_v * (l2 * math.sin(a2))
    # canvas.move(bob1, x1_v, y1_v)
    # canvas.move(bob2, x2_v, y2_v)
    # ln1 = canvas.create_line(px1, py1, x1, y1, fill="white")

    x1 = 450 + l1 * math.sin(a1)
    y1 = 200 + l1 * math.cos(a1)
    x2 = x1 + l2 * math.sin(a2)
    y2 = y1 + l2 * math.cos(a2)

    if px2 != -1:
        ln2 = canvas.create_line(px2, py2, x2, y2, width=3, fill="white")

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

    # create_circle(x1, y1, 1)
    # create_circle(x2,y2,3)

    a1_v += a1_a*0.1
    a2_v += a2_a*0.1
    a1 += a1_v*0.1
    a2 += a2_v*0.1

    px1 = x1
    py1 = y1
    px2 = x2
    py2 = y2

    clock += 1
    print(a1_a)
    time.sleep(0.0001)
    tk.update()

mainloop()
