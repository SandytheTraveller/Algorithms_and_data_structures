import turtle

def drawTriangle(points, colour, myTurtle):
    myTurtle.fillcolor(colour)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()

def getMidPoints(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'yellow', 'white', 'brown', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMidPoints(points[0], points[1]),
                    getMidPoints(points[0], points[2])], degree - 1, myTurtle)
    sierpinski([points[1],
                getMidPoints(points[0], points[1]),
                getMidPoints(points[1], points[2])], degree - 1, myTurtle)
    sierpinski([points[2],
                getMidPoints(points[2], points[1]),
                getMidPoints(points[0], points[2])], degree - 1, myTurtle)

def main():
    myTurtle = turtle.Turtle()
    myPoints = [[-500, -250], [0, 500], [500, -250]]
    sierpinski(myPoints, 3, myTurtle)

main()