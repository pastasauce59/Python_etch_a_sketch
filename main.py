from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(100)

screen.listen()
#When passing a function as the input, you only put the name without the invoking paranthesis at the end.
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()