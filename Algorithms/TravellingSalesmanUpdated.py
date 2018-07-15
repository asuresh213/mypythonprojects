from Tkinter import *
import cmath
import random
import math
import copy

# to see the actual numbers, find all "#print" and replace it with "print"

# ===================================== TOOLS ==============================================================


def dist(x1, y1, x2, y2):
    p1 = complex(x1, y1)
    p2 = complex(x2, y2)
    distance = abs(p2-p1)
    return distance


def create_circle(xm1, ym1, rad, citynum):
    canvas.create_oval(xm1-rad, ym1-rad, xm1+rad, ym1+rad, fill="white")
    # for i in range(citynum+1):
    # canvas.create_oval(xm1-rad-5*i, ym1-rad-5*i, xm1+rad+5*i, ym1+rad+5*i, outline="white")

# ===========================================================================================================


# =========================== LOOPING THROUGH CITIES AND CHANGING THE ARRAY =================================

def rotate_cities(cities_):
    # print(cities_, "This is cities under function")
    temp = cities_[0]
    for i in range(len(cities)-1):
        cities_[i] = cities_[i+1]
    cities_[len(cities_)-1] = temp
    return cities_

# ===========================================================================================================


# ====================================== DRAWING THE PATH ===================================================

def DrawPath(tempcities, canvas, tempdistance, cities, record_cities, Total_distance_array, sum):
    if(len(tempcities) == len(cities)):
        # print(len(tempcities), len(cities), "length of arrays")
        record_cities.append(list(tempcities))
    completed = False
    # print(tempcities, "This is TempCities under DrawPath")
    # print(record_cities, "This is RecordCities under DrawPath")
    for j in range(len(tempcities)):
        if(j != 0):
            tempdistance.append(dist(tempcities[0].real, tempcities[0].imag,
                                     tempcities[j].real, tempcities[j].imag))


# ----------------------------------- Initial case ---------------------------------------------------------
            if(len(tempdistance) == 1):
                recorddistance = dist(tempcities[0].real, tempcities[0].imag,
                                      tempcities[j].real, tempcities[j].imag)
                sum += recorddistance
                record_c2 = tempcities[j]
                record_index = j
# ----------------------------------------------------------------------------------------------------------


# ------------------------------------ Calculating the minimum distance ------------------------------------
            if(dist(tempcities[0].real, tempcities[0].imag, tempcities[j].real, tempcities[j].imag) < recorddistance):
                recorddistance = dist(tempcities[0].real, tempcities[0].imag,
                                      tempcities[j].real, tempcities[j].imag)
                record_c2 = tempcities[j]
                record_index = j
# -----------------------------------------------------------------------------------------------------------

    # print(tempcities[0], record_c2, record_index)  # check to see if we have all our values right


# --------------------------------Create edge between two cities with min distance --------------------------
    ln = canvas.create_line(tempcities[0].real, tempcities[0].imag, record_c2.real,
                            record_c2.imag, width=2, fill="white")

# -----------------------------------------------------------------------------------------------------------


# --------------------------------------------- Update ------------------------------------------------------
    del(tempcities[0])

    # print(tempcities)  # check to see if tempcities was deleted properly
    temp = tempcities[0]
    tempcities[0] = record_c2
    tempcities[record_index - 1] = temp

    # print(tempcities, "modified")  # check to see if tempcities was modified properly

    tempdistance = []  # resetting tempdistance so we do not overwrite in the next pass
    recorddistance = 0  # resetting recorddistance so we do not overwrite in the next pass
    record_c2 = 0  # resetting record_c2 so we do not overwrite in the next pass
    if(len(tempcities) > 1):
        # print(len(tempcities))
        DrawPath(tempcities, canvas, tempdistance, cities, record_cities, Total_distance_array, sum)
    else:
        Total_distance_array.append(sum)
        return list([record_cities, Total_distance_array])

# -----------------------------------------------------------------------------------------------
# ===============================================================================================


# ============================== DRAWING THE MOST OPTIMAL PATH ===================================

def FinalDrawPath(tempcities, canvas, distance):
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

    # print(tempcities[0], record_c2, record_index)
    # print(distance)
    ln = canvas.create_line(tempcities[0].real, tempcities[0].imag, record_c2.real,
                            record_c2.imag, width=3, fill="green")
    del(tempcities[0])

    # print(tempcities)
    temp = tempcities[0]
    tempcities[0] = record_c2
    tempcities[record_index - 1] = temp

    # print(tempcities, "modified")

    distance = []
    recorddistance = 0
    record_c2 = 0
    if(len(tempcities) > 1):
        FinalDrawPath(tempcities, canvas, distance)

# ======================================================================================================================



# ----------------------------------- GLOBAL VARIABLES -----------------------------------------
tempdistance = []
cities = []
tempcities = []
# -----------------------------------------------------------------------------------------------


# ------------------------------------- SETTING UP THE CANVAS -----------------------------------
tk = Tk()
my_color = '#%02x%02x%02x' % (0, 10, 15)
canvas = Canvas(tk, width=900, height=900, bg=my_color)
tk.title("Travelling Salesman")
canvas.pack()
# -----------------------------------------------------------------------------------------------


# ====================================== MAIN FUNCTION ==========================================

for i in range(5):
    cities.append(complex(random.randrange(100, 700), random.randrange(100, 700)))
    create_circle(cities[i].real, cities[i].imag, 3, i)

tempcities = list(cities)
# print(cities, "this is under main")
record_cities = []
Total_distance_array = []
infolist = []
for i in range(len(cities)):
    # print("\n", i, "this is i")  # Check to see if loop works fine
    tempdistance = []  # reinitializing tempdistance so we do not have any overwrite issues between different tempcities
    # Drawing the path between cities (with minimum distance)
    DrawPath(tempcities, canvas, tempdistance, cities,
             record_cities, Total_distance_array, 0)
    # print(infolist, "This is infolist")
    cities = rotate_cities(cities)  # rotate the cities list to construct a different path.
    tempcities = list(cities)  # redefine tempcities to pass into Drawpath
    # print(tempcities, "t----")  # check to see if tempcities is copied properly
    # print(cities, "c----")  # check to see if cities is returned properly

k = Total_distance_array.index(min(Total_distance_array))
# print(k)
# print(Total_distance_array)
# print(Total_distance_array[k])
# print(record_cities)
# print(record_cities[k])

FinalDrawPath(record_cities[k], canvas, [])

tk.update()
mainloop()

# =================================================================================================
