
import turtle
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

new_square = turtle.Turtle()
screen  = turtle.Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(600,600)
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down") 
screen.onkey(snake.left, "Left") 
screen.onkey(snake.right, "Right") 


game_is_on = True

while game_is_on:
     screen.update()
     time.sleep(0.1)
     snake.move()
     
      #Detect collision wih food
     if snake.head.distance(food) < 15:
          food.refresh()
          snake.extend()
          scoreboard.increase_score()
          
          
     #Detect collision with wall.
     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
   #Detect collision with tail.
     for segment in snake.segments[1: ]:
          if segment == snake.head:
            pass
          elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()