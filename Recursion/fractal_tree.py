import turtle as ts

ts.right(-90)
angle = 30
def drawY(size, level):
    if level > 0:
        ts.colormode(255)
        ts.pencolor(0, 255 // level, 0)
        # drawing the base
        ts.forward(size)
        ts.right(angle)
        # recursive call for the right subtree
        drawY(0.8 * size, level - 1)
        ts.pencolor(0, 255 // level, 0)
        ts.left(2 * angle)
        # recursive call for the left subtree
        drawY(0.8 * size, level - 1)
        ts.pencolor(0, 255 // level, 0)
        ts.right(angle)
        ts.forward(-size)
def main():
    myWin = ts.Screen()
    drawY(80, 12)
    myWin.exitonclick()

main()