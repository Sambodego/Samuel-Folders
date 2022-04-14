import turtle as t
playerAscore=0
playerBscore=0
playing = False
window=t.Screen()
leftpaddle=t.Turtle()
rightpaddle=t.Turtle()
ball=t.Turtle()
pen=t.Turtle()
ballxdirection = 0.2
ballydirection = 0.2


def init():
 
      #window specs
    window.title("Ping Pong")
    window.bgcolor("Green")
    window.setup(width=800,height=600)
    window.tracer(0)

    #create left paddle
    
    leftpaddle.speed(0)
    leftpaddle.shape("square")
    leftpaddle.color("White")
    leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
    leftpaddle.penup()
    leftpaddle.goto(-350,0)


    #create right paddle
    
    rightpaddle.speed(0)
    rightpaddle.shape("square")
    rightpaddle.color("White")
    rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
    rightpaddle.penup()
    rightpaddle.goto(350,0)

    #creating ball
    
    ball.speed(20)
    ball.shape("circle")
    ball.color("Red")
    ball.penup()
    ball.goto(5,5)
    

    #creating scorecard update
    
    pen.speed(0)
    pen.color("Blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("score", align="center", font=('Arial',24,'normal'))

    #Assign keys to play
    window.listen()
    window.onkeypress(leftpaddleup,'w')
    window.onkeypress(leftpaddledown,'s')
    window.onkeypress(rightpaddleup,'Up')
    window.onkeypress(rightpaddledown,'Down')
    window.onkeypress(play_pause, 'z')
    
#moving left paddle up
def leftpaddleup():
    if leftpaddle.ycor() < 250:
        y=leftpaddle.ycor()
        y=y+50
        leftpaddle.sety(y)


#moving left down
def leftpaddledown():
    if leftpaddle.ycor() > -250:
        y=leftpaddle.ycor()
        y=y-50
        leftpaddle.sety(y)
    
#moving right paddle
def rightpaddleup():
    if rightpaddle.ycor() < 250:
        y=rightpaddle.ycor()
        y=y+50
        rightpaddle.sety(y)

#moving paddle down
def rightpaddledown():
    if rightpaddle.ycor() > -250:
        y=rightpaddle.ycor()
        y=y-50
        rightpaddle.sety(y)

def play_pause():
    global playing
    if playing:
        playing = False
    else:
        playing = True 
   

init()



def runGame():
    global ballxdirection
    global ballydirection
    global playerAscore
    global playerBscore
    window.update()
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

  #####**********************************  
    #setting up boarder
    if ball.ycor()>290:
        ballydirection=ballydirection*-1
        ball.sety(ball.ycor()+ballydirection)

    if ball.ycor() < -290:
        ballydirection=ballydirection*-1
        ball.sety(ball.ycor()+ballydirection)
          
    if ball.xcor() > 340:
        play_pause()
        ball.sety(0)
        ball.setx(0)
        setLose() 
        init()
        playerAscore=playerAscore+1
    

    if ball.xcor() < -340:
        play_pause()
        ball.sety(0)
        ball.setx(0)
        setLose() 
        init()
        playerBscore=playerBscore+1
        # pen.clear()
        # pen.write("player A:{}   player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

    # print(rightpaddle.ycor())

    if (ball.xcor() > 339.9) and (ball.xcor() < 340) and (ball.ycor()>=rightpaddle.ycor()-55) and (ball.ycor()<=rightpaddle.ycor()+55):
        ballxdirection = ballxdirection * -1
  
    if (ball.xcor() < -339.9) and (ball.xcor() > -340) and (ball.ycor()>=leftpaddle.ycor()-55) and (ball.ycor()<=leftpaddle.ycor()+55):
        ballxdirection = ballxdirection * -1

    pen.clear()
    pen.write("player A:{}   player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))

#while True:
#    window.update()
 #   if playing:
  #      runGame()