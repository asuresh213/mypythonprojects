from Tkinter import *
import time
import math


def create_circle(xm1, ym1, rad):
    canvas.create_oval(xm1-rad, ym1-rad, xm1+rad, ym1+rad, outline="white")


tk = Tk()
canvas = Canvas(tk, width=600, height=400, bg="black")
tk.title("Fourier")
canvas.pack()

w1 = Scale(tk, from_=1, to=10, orient=HORIZONTAL)
w1.set(1)
w1.pack()

clock = 0

wave = []
while clock < 1000:
    x = 200
    y = 200

    for i in range(w1.get()):
        prevx = x
        prevy = y
        n = 2*i + 1
        radius = 50*(4/(n*math.pi))
        x += radius*math.cos(n * clock)
        y += radius*math.sin(n * clock)

        create_circle(prevx, prevy, radius)

        canvas.create_line(prevx, prevy, x, y, fill="white")
        # canvas.create_oval(x-2,y-2,x+2,y+2,fill="white")

    wave.insert(0, y)
    canvas.create_line(x, y, 400, wave[0], fill="white")
    for i in range(len(wave)):
        if(i == 0):
            create_circle(400+i, wave[i], 1)
        else:
            canvas.create_line(399+i, wave[i-1], 400+i, wave[i], width=2, fill="white")

    # updating the loop
    clock += 0.03
    time.sleep(0.0001)
    tk.update()
    canvas.delete("all")
    if(len(wave) > 500):
        del(wave[-1])
mainloop()
