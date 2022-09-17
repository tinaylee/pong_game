from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_R = (350, 0)
PADDLE_L = (-350, 0)
SCORE_L = (-100, 230)
SCORE_R = (100, 230)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score_l = Scoreboard(SCORE_L)
score_l.display_score()
score_r = Scoreboard(SCORE_R)
score_r.display_score()

paddle_l = Paddle(PADDLE_L)
paddle_r = Paddle(PADDLE_R)

ball = Ball()


screen.listen()
#Move Left paddle up and down
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

#Move Right paddle up and down
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    #Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()

    #Detect if right paddle missed
    if ball.xcor() > 340:
        new_score = score_l.increment_score()
        score_r.display_score()
        ball.restart()


    #Detect if left paddle missed
    if ball.xcor() < -340:
        new_score = score_r.increment_score()
        score_l.display_score()
        ball.restart()
        speed = 0.1

screen.exitonclick()