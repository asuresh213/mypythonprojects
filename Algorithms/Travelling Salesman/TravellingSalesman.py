from Tkinter import *
import cmath
import random
import math
# -------------------------------------- TOOLS --------------------------------------------------


def dist(x1, y1, x2, y2):
    p1 = complex(x1, y1)
    p2 = complex(x2, y2)
    distance = abs(p2-p1)
    return distance


def create_circle(xm1, ym1, rad, citynum):
    canvas.create_oval(xm1-rad, ym1-rad, xm1+rad, ym1+rad, fill="white")
    # for i in range(citynum+1):
    #canvas.create_oval(xm1-rad-5*i, ym1-rad-5*i, xm1+rad+5*i, ym1+rad+5*i, outline="white")

# ------------------------------------------------------------------------------------------------


def rotate_cities(cities_):
    temp = cities_[0]
    for i in range(len(cities)-1):
        cities_[i] = cities_[i+1]
    cities_[len(cities_)-1] = temp
    return cities_


def Console(cities, tempcities, canvas, distance):
    # for i in range(len(cities)):
    DrawPath(tempcities, canvas, distance)
    #cities = rotate_cities(cities)
    #tempcities = cities
    #DrawPath(tempcities, canvas, distance)


def DrawPath(tempcities, canvas, distance):
    # print(tempcities)
    for j in range(len(tempcities)):
        if(j != 0):
            distance.append(dist(tempcities[0].real, tempcities[0].imag,
                                 tempcities[j].real, tempcities[j].imag))
            if(len(distance) == 1):
                recorddistance = dist(tempcities[0].real, tempcities[0].imag,
                                      tempcities[j].real, tempcities[j].imag)
                record_c2 = tempcities[j]
                record_index = j
            if(dist(tempcities[0].real, tempcities[0].imag, tempcities[j].real, tempcities[j].imag) < recorddistance):
                recorddistance = dist(tempcities[0].real, tempcities[0].imag,
                                      tempcities[j].real, tempcities[j].imag)
                record_c2 = tempcities[j]
                record_index = j

    #print(tempcities[0], record_c2, record_index)
    # print(distance)
    ln = canvas.create_line(tempcities[0].real, tempcities[0].imag, record_c2.real,
                            record_c2.imag, width=2, fill="white")
    del(tempcities[0])

    # print(tempcities)
    temp = tempcities[0]
    tempcities[0] = record_c2
    tempcities[record_index - 1] = temp

    #print(tempcities, "modified")

    distance = []
    recorddistance = 0
    record_c2 = 0
    if(len(tempcities) > 1):
        DrawPath(tempcities, canvas, distance)


distance = []
cities = []
tempcities = []
tk = Tk()
my_color = '#%02x%02x%02x' % (0, 10, 15)
canvas = Canvas(tk, width=900, height=900, bg=my_color)
tk.title("Travelling Salesman")
canvas.pack()
for i in range(9):
    cities.append(complex(random.randrange(100, 700), random.randrange(100, 700)))
    create_circle(cities[i].real, cities[i].imag, 3, i)
tempcities = cities
Console(cities, tempcities, canvas, [])


tk.update()
mainloop()
