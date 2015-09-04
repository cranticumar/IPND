import turtle

def draw_square(distance):
    '''
    Draw a square of length = distance
    '''
    for i in range(4):
        ninja.forward(distance)
        ninja.right(90)

def draw_circle(radius):
    '''
    Draw a circle fo radius
    '''
    ninja.circle(radius)

def draw_triangle(a=60, b=60, angle=60):
    '''
    Draw an equilateral triange unless distances specified
    '''
    posi = ninja.pos()
    ninja.backward(a)
    ninja.right(angle)
    ninja.forward(b)
    ninja.goto(posi)

def draw_polygon(a, b, c, d):
    for angle in [a, b, c, d]:
        ninja.forward(50)
        ninja.right(angle)

ninja = turtle.Turtle()
ninja.speed('normal')
ninja.shape('turtle')
ninja.color('yellow')
pos = ninja.position()
window = turtle.Screen()
window.bgcolor('red')

angle = 0
while angle != 360:
    draw_polygon(45, 135, 45, 135)
    ninja.right(10)
    angle = angle + 10
ninja.right(90)
ninja.forward(200)

# draw_circle(100)
# draw_triangle()

window.exitonclick()