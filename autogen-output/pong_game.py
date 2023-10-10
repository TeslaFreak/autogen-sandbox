import turtle

# Set up the game window
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Create the paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


# Function to move paddle a up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)


# Function to move paddle a down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)


# Function to move paddle b up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)


# Function to move paddle b down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)


# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with paddles
    if (
        (ball.dx > 0)
        and (350 > ball.xcor() > 340)
        and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50)
    ):
        ball.setx(340)
        ball.color("blue")
        ball.dx *= -1

    elif (
        (ball.dx < 0)
        and (-350 < ball.xcor() < -340)
        and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50)
    ):
        ball.setx(-340)
        ball.color("red")
        ball.dx *= -1

    # Check for collision with top and bottom walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Check for winning condition
    if ball.xcor() > 390:
        print("Player A wins!")
        break

    elif ball.xcor() < -390:
        print("Player B wins!")
        break

# Terminate the game
turtle.done()
turtle.bye()
