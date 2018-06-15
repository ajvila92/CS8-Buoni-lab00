# Angelo Vila
# June 9, 2018

import turtle
t = turtle.Turtle('turtle') # create Turtle object for drawing

# my example code that draws a star
t.up() # lift turtl's tail
t.setposition(-100, -100) # move turtle down 100 and left 100 from origin
t.down() # lower turtle's tail
t.pencolor('blue') # set pen color
t.width(3) # set pen width to 3 pixels
t.fillcolor('red') # set fill color
t.setheading(36) # set inital head of turtle
t.begin_fill() # start fill

# move around perimeter of star
t.forward(100)
t.right(72)
t.forward(100)
t.left(144)

t.forward(100)
t.right(72)
t.forward(100)
t.left(144)

t.forward(100)
t.right(72)
t.forward(100)
t.left(144)

t.forward(100)
t.right(72)
t.forward(100)
t.left(144)

t.forward(100)
t.right(72)
t.forward(100)
t.left(144)

t.end_fill() # end fill

s = turtle.Screen() # create Screen object
s.exitonclick() # prevents turtle window from "freezing up"
