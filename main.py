from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

y_cord = -70
color_num = 0
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cord) 
    new_turtle.color(colors[color_num])
    all_turtles.append(new_turtle)
    color_num += 1
    y_cord += 30
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You WON! The winning turtle is {winning_turtle}.")
            else:
                print(f"You lose. The winning turtle is {winning_turtle}.")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    
screen.exitonclick()