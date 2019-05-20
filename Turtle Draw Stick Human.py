import turtle

my_screen = turtle.Screen()
my_screen.setup(0.5,0.75,0,0)
my_turtle = turtle.Turtle()

def draw_head(xposition,yposition,radius):
    my_turtle.setx(xposition)
    my_turtle.sety(yposition)
    my_turtle.pd()
    my_turtle.circle(radius)

def draw_body(bodylength):
    my_turtle.setheading(270)
    my_turtle.fd(bodylength)

def draw_right_leg(rightleglength):
    my_turtle.setheading(300)
    my_turtle.fd(rightleglength)
    my_turtle.setheading(120)
    my_turtle.fd(rightleglength)

def draw_left_leg(leftleglength,bodylength):
    my_turtle.setheading(240)
    my_turtle.fd(leftleglength)
    my_turtle.setheading(60)
    my_turtle.fd(leftleglength)
    my_turtle.setheading(90)
    my_turtle.fd(bodylength/2)

def draw_right_arm(rightarmlength):
    my_turtle.setheading(300)
    my_turtle.fd(rightarmlength)
    my_turtle.setheading(120)
    my_turtle.fd(rightarmlength)

def draw_left_arm(leftarmlength):
    my_turtle.setheading(240)
    my_turtle.fd(leftarmlength)

def drawstickman(xposition, yposition, radius,bodylength,rightleglength,leftleglength,rightarmlength,leftarmlength):
   
    draw_head(xposition,yposition,radius)
    draw_body(bodylength)
    draw_right_leg(rightleglength)
    draw_left_leg(leftleglength,bodylength)
    draw_right_arm(rightarmlength)
    draw_left_arm(leftarmlength)
    my_turtle.setheading(0)
    my_turtle.pu()

drawstickman(0,0,100,100,100,100,100,100)
drawstickman(100,100,100,100,100,100,100,100)
    

    
