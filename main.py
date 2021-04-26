from graphics import *


def main():
    global win
    win = GraphWin("Burgos_82874, GAME!", 400, 400)
    prepare_game()
    losing_squares()
    rectangle_entries()

#commit change test


def rectangle_entries():

    for i in range(10):
        p = win.getMouse()
        x1 = p.getX() - 10
        y1 = p.getY() - 10
        x2 = p.getX() + 10
        y2 = p.getY() + 10
        r = Rectangle(Point(x1, y1), Point(x2, y2))
        r.setFill("red")
        r.setOutline("red")
        r.setWidth(0)
        r.draw(win)

def losing_squares():



    for i in range(10):
        r = Rectangle(Point(20, 20), Point(40, 40))
        r.setFill("red")
        r.setOutline("red")
        r.setWidth(0)
        r.draw(win)


def prepare_game():

    v1 = Line(Point(20, 20), Point(380, 20))
    v2 = Line(Point(20, 40), Point(380, 40))
    v3 = Line(Point(20, 60), Point(380, 60))
    v4 = Line(Point(20, 80), Point(380, 80))
    v5 = Line(Point(20, 100), Point(380, 100))
    v6 = Line(Point(20, 120), Point(380, 120))
    v7 = Line(Point(20, 140), Point(380, 140))
    v8 = Line(Point(20, 160), Point(380, 160))
    v9 = Line(Point(20, 180), Point(380, 180))
    v10 = Line(Point(20, 200), Point(380, 200))
    v11 = Line(Point(20, 220), Point(380, 220))
    v12 = Line(Point(20, 240), Point(380, 240))
    v13 = Line(Point(20, 260), Point(380, 260))
    v14 = Line(Point(20, 280), Point(380, 280))
    v15 = Line(Point(20, 300), Point(380, 300))
    v16 = Line(Point(20, 320), Point(380, 320))
    v17 = Line(Point(20, 340), Point(380, 340))
    v18 = Line(Point(20, 360), Point(380, 360))
    v19 = Line(Point(20, 380), Point(380, 380))

    h1 = Line(Point(20, 380), Point(20, 20))
    h2 = Line(Point(40, 380), Point(40, 20))
    h3 = Line(Point(60, 380), Point(60, 20))
    h4 = Line(Point(80, 380), Point(80, 20))
    h5 = Line(Point(100, 380), Point(100, 20))
    h6 = Line(Point(120, 380), Point(120, 20))
    h7 = Line(Point(140, 380), Point(140, 20))
    h8 = Line(Point(160, 380), Point(160, 20))
    h9 = Line(Point(180, 380), Point(180, 20))
    h10 = Line(Point(200, 380), Point(200, 20))
    h11 = Line(Point(220, 380), Point(220, 20))
    h12 = Line(Point(240, 380), Point(240, 20))
    h13 = Line(Point(260, 380), Point(260, 20))
    h14 = Line(Point(280, 380), Point(280, 20))
    h15 = Line(Point(300, 380), Point(300, 20))
    h16 = Line(Point(320, 380), Point(320, 20))
    h17 = Line(Point(340, 380), Point(340, 20))
    h18 = Line(Point(360, 380), Point(360, 20))
    h19 = Line(Point(380, 380), Point(380, 20))

    v1.setOutline("black")
    v2.setOutline("black")
    v3.setOutline("black")
    v4.setOutline("black")
    v5.setOutline("black")
    v6.setOutline("black")
    v7.setOutline("black")
    v8.setOutline("black")
    v9.setOutline("black")
    v10.setOutline("black")
    v11.setOutline("black")
    v12.setOutline("black")
    v13.setOutline("black")
    v14.setOutline("black")
    v15.setOutline("black")
    v16.setOutline("black")
    v17.setOutline("black")
    v18.setOutline("black")
    v19.setOutline("black")

    h1.setOutline("black")
    h2.setOutline("black")
    h3.setOutline("black")
    h4.setOutline("black")
    h5.setOutline("black")
    h6.setOutline("black")
    h7.setOutline("black")
    h8.setOutline("black")
    h9.setOutline("black")
    h10.setOutline("black")
    h11.setOutline("black")
    h12.setOutline("black")
    h13.setOutline("black")
    h14.setOutline("black")
    h15.setOutline("black")
    h16.setOutline("black")
    h17.setOutline("black")
    h18.setOutline("black")
    h19.setOutline("black")

    v1.draw(win)
    v2.draw(win)
    v3.draw(win)
    v4.draw(win)
    v5.draw(win)
    v6.draw(win)
    v7.draw(win)
    v8.draw(win)
    v9.draw(win)
    v10.draw(win)
    v11.draw(win)
    v12.draw(win)
    v13.draw(win)
    v14.draw(win)
    v15.draw(win)
    v16.draw(win)
    v17.draw(win)
    v18.draw(win)
    v19.draw(win)

    h1.draw(win)
    h2.draw(win)
    h3.draw(win)
    h4.draw(win)
    h5.draw(win)
    h6.draw(win)
    h7.draw(win)
    h8.draw(win)
    h9.draw(win)
    h10.draw(win)
    h11.draw(win)
    h12.draw(win)
    h13.draw(win)
    h14.draw(win)
    h15.draw(win)
    h16.draw(win)
    h17.draw(win)
    h18.draw(win)
    h19.draw(win)


main()
