import turtle

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(800, 600)

ascore = 0
bscore = 0

lpaddle = turtle.Turtle()
lpaddle.shape("square")
lpaddle.color("white")
lpaddle.speed(0)
lpaddle.shapesize(stretch_wid=5, stretch_len=1)
lpaddle.penup()
lpaddle.goto(-350,0)

rpaddle = turtle.Turtle()
rpaddle.shape("square")
rpaddle.color("white")
rpaddle.speed(0)
rpaddle.shapesize(stretch_wid=5, stretch_len=1)
rpaddle.penup()
rpaddle.goto(350,0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5,5)
ballxdirection = 7
ballydirection = 7

write=turtle.Turtle()
write.color("green")
write.penup()
write.hideturtle()
write.goto(0,260)
write.write("SCORE: 0 - 0", align="center")

def lup():
    y = lpaddle.ycor()
    y += 30
    if lpaddle.ycor()<220:
        lpaddle.sety(y)
def ldown():
    y = lpaddle.ycor()
    y -= 30
    if lpaddle.ycor()>-220:
        lpaddle.sety(y)

def rup():
    y = rpaddle.ycor()
    y += 30
    if rpaddle.ycor() <220:
        rpaddle.sety(y)

def rdown():
    y = rpaddle.ycor()
    y -= 30
    if rpaddle.ycor() > -220:
        rpaddle.sety(y)

i=0

window.listen()
window.onkeypress(lup,'w')
window.onkeypress(ldown,'s')
window.onkeypress(rup,'Up')
window.onkeypress(rdown, 'Down')

while True:
    window.update()

    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    if ball.xcor()>380:
        ball.goto(0,0)
        ascore += 1
        write.clear()
        write.write("SCORE: {} - {}".format(ascore, bscore), align="center")

    if ball.xcor()<-390:
        ball.goto(0,0)
        bscore += 1
        write.clear()
        write.write("SCORE: {} - {}".format(ascore, bscore), align="center")

    if ball.ycor()>285:
        ballydirection=ballydirection*-1

    if ball.ycor()<-280:
        ballydirection = ballydirection*-1

    if ball.xcor()>330 and ball.xcor()<340 and ball.ycor()<rpaddle.ycor()+45 and ball.ycor()>rpaddle.ycor()-45:
        ballxdirection = ballxdirection*-1
    if ball.xcor()<-330 and ball.xcor()>-340 and ball.ycor()<lpaddle.ycor()+45 and ball.ycor()>lpaddle.ycor()-45:
        ballxdirection = ballxdirection*-1

