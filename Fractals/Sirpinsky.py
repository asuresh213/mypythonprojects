from Tkinter import *
import cmath
import time


def midpt(x1, y1, x2, y2):
    x1_new = abs((x2 + x1)/2)
    y1_new = abs((y2 + y1)/2)
    return complex(x1_new, y1_new)


def Draw(layers, v1, v2, v3):
    while(layers > 0):
        v1_new = midpt(v2.real, v2.imag, v1.real, v1.imag)
        v2_new = midpt(v2.real, v2.imag, v3.real, v3.imag)
        v3_new = midpt(v1.real, v1.imag, v3.real, v3.imag)
        canvas.create_polygon(v1_new.real, v1_new.imag, v2_new.real, v2_new.imag,
                              v3_new.real, v3_new.imag, outline="white", width=2)
        layers -= 1
        Draw(layers, v1, v1_new, v3_new)
        Draw(layers, v2, v2_new, v1_new)
        Draw(layers, v3, v2_new, v3_new)
        root.update()
        time.sleep(0.01)


root = Tk()
canvas = Canvas(root, bg="black", height=600, width=600)
root.title("Sirprinsky")
canvas.pack()
layers = 6
canvas.create_polygon(300, 100, 100, 500, 500, 500, outline="white", width=2)
v1 = complex(300, 100)
v2 = complex(100, 500)
v3 = complex(500, 500)
Draw(layers, v1, v2, v3)


mainloop()
