import turtle
t = turtle
t.shape('turtle')
t.penup()
t.goto(0,220)
t.pendown()

t.setheading(0)
#turtle.bgcolor("black")
#t.color("white")
n = 500
size = 45
t.speed(0)
for i in range(n):
    t.circle(size)
    size = 0.99*size
    #t.penup()
    t.right(11)
    t.forward(size)
    t.pendown()

t.penup()
t.goto(250,-250)


t.mainloop()
