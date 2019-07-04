from Tkinter import *
import time
import random
import math


def create_circle(xm1, ym1, rad):
    canvas.create_oval(xm1-rad, ym1-rad, xm1+rad, ym1+rad, outline="white")


def dft(vals):
    X = []
    N = len(vals)
    for k in range(N):
        re = 0
        im = 0
        for n in range(N):
            arg = (2*math.pi*k*n)/N
            re += vals[n]*(math.cos(arg))
            im -= vals[n]*(math.sin(arg))
        re = re/N
        im = im/N
        amp = math.sqrt(re**2 + im**2)
        if(re != 0):
            phase = math.atan(im/re)
        else:
            phase = math.pi/2
        freq = k
        X.append([re, im, amp, phase, freq])
    return X


def epicycles(x, y, rotation, clock, fourier):
    for i in range(len(fourier)):
        prevx = x
        prevy = y
        freq = fourier[i][4]
        radius = fourier[i][2]
        phase = fourier[i][3]
        x += radius*math.cos(freq * clock + phase + rotation)
        y += radius*math.sin(freq * clock + phase + rotation)
        create_circle(prevx, prevy, radius)
        canvas.create_line(prevx, prevy, x, y, fill="white")
        # canvas.create_oval(x-2,y-2,x+2,y+2,fill="white")
    return [x, y]


tk = Tk()
canvas = Canvas(tk, width=600, height=400, bg="black")
tk.title("Fourier")
canvas.pack()


clock = 0
x = []
y = []

for i in range(100):
    anglex = i*2*math.pi/50
    x.append(50*math.cos(anglex))
    # x.append(random.randrange(0,100))
for j in range(100):
    angley = j*2*math.pi/50
    y.append(50*math.sin(angley))
    # y.append(random.randrange(0,100))

print(x)
print(y)
fourierY = dft(y)
fourierX = dft(x)
path = []
while clock < 1000:
    vx = epicycles(400, 50, 0, clock, fourierX)
    vy = epicycles(50, 200, math.pi/2, clock, fourierY)
    v = [vx[0], vy[1]]
    path.insert(0, v)
    canvas.create_line(vx[0], vx[1], path[0][0], path[0][1], fill="white")
    canvas.create_line(vy[0], vy[1], path[0][0], path[0][1], fill="white")
    # print(path)
    for i in range(len(path)):
        if(i == 0):
            create_circle(path[i][0], path[i][1], 1)
        else:
            canvas.create_line(path[i][0], path[i][1], path[i-1][0],
                               path[i-1][1], width=2, fill="white")

    # updating the loop
    dt = 2*math.pi/len(fourierX)
    clock += dt
    time.sleep(0.0001)
    tk.update()
    canvas.delete("all")
    # if(len(wave) > 500):
    # del(wave[-1])
mainloop()
