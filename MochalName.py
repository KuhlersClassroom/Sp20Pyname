from turtle import *
canvas = Screen()
canvas.setup(1000, 400)
spenser = Turtle()
spenser.shape("turtle")
spenser.color("green")
# ^ This is the setup stuff.

spenser.penup()
spenser.goto(-300, 75)
spenser.pendown()
spenser.backward(70)
spenser.right(90)
spenser.forward(50)
spenser.left(90)
spenser.forward(70)
spenser.right(90)
spenser.forward(50)
spenser.right(90)
spenser.forward(70)
# ^ The letter S

spenser.penup()
spenser.goto(-180, 75)
spenser.pendown()
spenser.forward(70)
spenser.backward(70)
spenser.right(90)
spenser.backward(50)
spenser.left(90)
spenser.forward(70)
spenser.right(90)
spenser.forward(50)
spenser.backward(100)
spenser.left(90)
# ^ The letter P

spenser.penup()
spenser.goto(-60, 75)
spenser.pendown()
spenser.forward(70)
spenser.left(90)
spenser.forward(50)
spenser.left(90)
spenser.forward(70)
spenser.backward(70)
spenser.right(90)
spenser.forward(50)
spenser.left(90)
spenser.forward(70)
spenser.left(180)
# ^ The letter E

spenser.penup()
spenser.goto(60, 75)
spenser.pendown()
spenser.left(90)
spenser.forward(100)
spenser.goto(-10, 75)
spenser.forward(100)
spenser.right(90)
# ^ The letter N

spenser.penup()
spenser.goto(180, 75)
spenser.pendown()
spenser.left(180)
spenser.backward(70)
spenser.right(90)
spenser.forward(50)
spenser.left(90)
spenser.forward(70)
spenser.right(90)
spenser.forward(50)
spenser.right(90)
spenser.forward(70)
# ^ The second letter S

spenser.penup()
spenser.goto(300, 75)
spenser.pendown()
spenser.forward(70)
spenser.left(90)
spenser.forward(50)
spenser.left(90)
spenser.forward(70)
spenser.backward(70)
spenser.right(90)
spenser.forward(50)
spenser.left(90)
spenser.forward(70)
spenser.left(180)
# ^ The second letter E

spenser.penup()
spenser.goto(420, 75)
spenser.pendown()
spenser.forward(70)
spenser.backward(70)
spenser.right(90)
spenser.backward(50)
spenser.left(90)
spenser.forward(70)
spenser.right(90)
spenser.forward(50)
spenser.backward(100)
spenser.left(90)
spenser.right(180)
spenser.penup()
spenser.forward(70)
spenser.pendown()
spenser.goto(350, 25)
# ^ The letter R

spenser.penup()
spenser.forward(100)
# ^ Just a little cleanup so you can see the letters cleanly! :D
