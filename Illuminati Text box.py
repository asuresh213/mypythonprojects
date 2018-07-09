from graphics import *

def Truth():
    string = 'Illuminati is the one true meaning of life'
    win.setBackground(color_rgb(255, 255, 255))
    txt = Text(Point(250, 225), "What is life?")
    txt.draw(win)

    input_box = Entry(Point(250,250), 50)
    input_box.draw(win)
    txt1 = Text(Point(150, 275), "Message translated to Machine Language:")
    txt1.draw(win)
    txt2 = Text(Point(360, 275), "")
    txt2.draw(win)

    #disc = Text(Point(250, 490), "Hit space to exit")
    #disc.draw(win)

    while len(input_box.getText()) <= 43:
        k = len(input_box.getText())
        txt2.setText(string[0:k])

    img = Image(Point(250, 250), "Efm8EiU.gif")
    img.draw(win)

    win.getMouse()
    win.close()

win = GraphWin("Truth", 500, 500)
Truth()