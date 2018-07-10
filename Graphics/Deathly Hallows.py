import math

from graphics import *


def DeathlyHallows():
    win.setBackground(color_rgb(0,10,15))
    pt = Point(250,250)
    #pt.setOutline(color_rgb(255,255,255))
    #pt.draw(win)

    poly = Polygon(Point(250, 150), Point(250+int(50*math.sqrt(3)), 250+50), Point(250-int(50*math.sqrt(3)), 250+50))
    poly.setWidth(2)
    poly.setOutline(color_rgb(255,255,255))
    poly.draw(win)

    cir = Circle(pt, 50)
    cir.setWidth(2)
    cir.setOutline(color_rgb(255, 255, 255))
    cir.draw(win)

    ln = Line(Point(250,150), Point(250,300))
    ln.setWidth(2)
    ln.setOutline(color_rgb(255, 255, 255))
    ln.draw(win)

    win.getMouse()
    win.close()






win = GraphWin("Deathly Hallows", 500, 500)
DeathlyHallows()