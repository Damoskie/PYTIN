import turtle

# Function to draw a polygon with n sides and side length
def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(angle)

# Set up the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Speed up the drawing process
t.speed(3)

# Example: Draw polygons with various sides
# Square (4 sides)
draw_polygon(4, 100)

# Move to a new position
t.penup()
t.goto(-150, 0)
t.pendown()

# Triangle (3 sides)
draw_polygon(3, 100)

# Move to a new position
t.penup()
t.goto(150, 0)
t.pendown()

# Pentagon (5 sides)
draw_polygon(5, 100)

# Move to a new position
t.penup()
t.goto(0, -150)
t.pendown()

# Hexagon (6 sides)
draw_polygon(6, 100)

# Hide the turtle after drawing
t.hideturtle()

# Finish up
screen.mainloop()
