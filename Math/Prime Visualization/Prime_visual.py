from Tkinter import *
import math
import Primes

angle = 0
w = 1080
h = 800
tk = Tk()
canvas = Canvas(tk, width=w, height=h, bg='black')
tk.title("Primes")
canvas.pack()


originx = w/2
originy = h/2

for i in range(len(Primes.primes)):
    my_color = "#%20x%20x%20x" % (int(i/len(Primes.primes)),
                                  int((i)/len(Primes.primes)), int((i)/len(Primes.primes)))
    r = Primes.primes[i]/275
    x = r*math.cos(angle)
    y = r*math.sin(angle)
    canvas.create_oval(originx + x, originy + y, originx + x, originy + y, width=0, fill='grey')
    angle += i

mainloop()
