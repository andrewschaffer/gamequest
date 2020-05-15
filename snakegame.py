#SNAKE - ANDREW SCHAFFER - COMPSCI / COZORT/ PERIOD 2
# 
#  credit/inspiration - @TokyoEdTech


#imports for game functions
import turtle
import time
import random



#small delay 
delay = 0.1

# Score / start at zero
score = 0
high_score = 0

# general setup for the game
snakegame = turtle.Screen()
snakegame.title("Snake Game")
snakegame.bgcolor("lime green")
snakegame.setup(width=700, height=700)
snakegame.tracer(0) # Turns off the screen updates

# Snake head
#this is the thing the player controls
#general setup and spawn
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
#initial spawn and colors/shapes
food = turtle.Turtle()
food.shape("circle")
food.color("purple")
food.penup()
food.goto(0,100)

segments = []

# follow up behind the turtle 
follow = turtle.Turtle()
follow.speed(0)
follow.shape("square")
follow.color("blue")
follow.penup()
follow.hideturtle()
follow.goto(0, 260)
follow.write("Welcome to Snake, use WASD to control your snake", align="center", font=("comic sans", 18, "normal"))

# Functions
# general movement
#defining the functions of up, down, left, right
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
snakegame.listen()
snakegame.onkeypress(go_up, "w")
snakegame.onkeypress(go_down, "s")
snakegame.onkeypress(go_left, "a")
snakegame.onkeypress(go_right, "d")

# Main game loop
while True:
    snakegame.update()

    # true border setup / marking collision area
    if head.xcor()>300 or head.xcor()<-300 or head.ycor()>300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        follow.clear()
        follow.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Collision for center of food, within 20 pixels counts... makes for some clipping 
    if head.distance(food) < 20:
        # Move the food to a random spot
        #it is within the 700*700 border to eliminate border spawns so the game can be competed
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x,y)

        # Command for when a snake eats food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay of spawns
        delay -= 0.001

        # Increase score by 1 per food eaten
        score += 1

        if score > high_score:
            high_score = score
        
        follow.clear()
        follow.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    # prevent hitting body
    # remove old coordinates to a far coordinate out of the border ... deleting was a hassle and would break the loop
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            follow.clear()
            follow.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

snakegame.mainloop()