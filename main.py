from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    score.score_board()
    snake.move()

    #Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.change_score()
    
    #Detect Collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        score.game_over()
        game_on = False
    elif snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_on = False

    #Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()





screen.exitonclick()
