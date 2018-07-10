import math

from graphics import *


def drawstuff(num):

    win.setBackground(color_rgb(0, 10, 15))

    """Center of the Circle"""
    pt = Point(350, 350)
    pt.setFill(color_rgb(255, 255, 255))
    pt.draw(win)

    """Right bottom vertex of Equilateral Triangle"""
    pt2 = Point(350+int((50*math.sqrt(3))), 350+50)
    pt2.setOutline(color_rgb(0, 0, 0))
    #pt2.draw(win)

    """Left bottom vertex of Equilateral Triangle"""
    pt3 = Point(350 - int((50 * math.sqrt(3))), 350 + 50)
    pt3.setOutline(color_rgb(0, 0, 0))
    #pt3.draw(win)

    """Top vertex of equilateral triangle"""
    pt4 = Point(350, 250)
    pt4.setOutline(color_rgb(0, 0, 0))
    #pt4.draw(win)

    """Circle with (max)radius 100"""
    cir = Circle(pt, num)
    cir.setOutline(color_rgb(250, 250, 250))
    cir.setWidth(2)
    cir.draw(win)
    cir.undraw()
    if(num == 100):
        cir.draw(win)

    """Lines going from the center of the circle to the vertices of the Triangle"""
    ln = Line(Point(350, 350), Point(350+int((50*math.sqrt(3))), 350+50))
    ln1 = Line(Point(350, 350), Point(350 - int((50 * math.sqrt(3))), 350 + 50))
    ln2 = Line(Point(350, 350), Point(350, 250))
    ln.setWidth(2)
    ln1.setWidth(2)
    ln2.setWidth(2)
    ln.setOutline(color_rgb(255, 255, 255))
    ln1.setOutline(color_rgb(255, 255, 255))
    ln2.setOutline(color_rgb(255, 255, 255))
    ln.draw(win)
    ln1.draw(win)
    ln2.draw(win)
    #ln.undraw()
    #if (num == 100):
        #ln.draw(win)

    """Drawing a square around the circle"""
    rect = Rectangle(Point(250, 250), Point(450, 450))
    rect.setWidth(2)
    rect.setOutline(color_rgb(255, 255, 255))
    rect.draw(win)

    """Drawing the triangle"""
    poly = Polygon(pt2, pt3, pt4)
    poly.setOutline(color_rgb(250, 250, 250))
    poly.setWidth(2)
    poly.draw(win)

    txt = Text(Point(350, 225), "Symmetries are amazing!")
    txt.setTextColor(color_rgb(255, 255, 255))
    txt.setSize(15)
    txt.draw(win)

    img = Image(Point(575, 575), "Efm8EiU.gif")
    img.draw(win)


win = GraphWin("My Window", 700, 700)
# for i in range(101):
i = 100
drawstuff(i)

win.getMouse()
win.close()
