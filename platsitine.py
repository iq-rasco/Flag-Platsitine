from turtle import *
speed(4)
  
setup(800, 400)


penup()


goto(-400, 200)


pendown()


color("black")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()


color("white")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()


color("green")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()


color("red")
begin_fill()
goto(-200, 20)
left(320)
forward(-400)
end_fill()


mainloop()
