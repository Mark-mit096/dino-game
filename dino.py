
from re import T
import turtle 
import random

window = turtle.Screen()
window.title("dinow game")
window.setup(width=1000,height=150)

dyu=turtle.Turtle()
dyu.color("red")
dyu.penup()
dyu.goto(200,0)
dinow=turtle.Turtle()
dinow.penup()
dead=turtle.Turtle()
dead.color("red")
dead.penup()
dead.goto(-200,0)
grass=turtle.Turtle()
grass.speed(0)

tre=turtle.Turtle()
tre.penup()
tre.speed(0)
tre.goto(400,-30)
tre.pendown()
tre.begin_fill()
tre.fillcolor('brown')
tre.goto(400,20)
tre.goto(410,20)
tre.goto(410,-30)
tre.end_fill()
tre.hideturtle()
tre.begin_fill()
tre.fillcolor('green')
tre.penup()
tre.goto(410,20)
tre.pendown()
tre.goto(420,20)
tre.goto(420,40)
tre.goto(390,40)
tre.goto(390,20)
tre.goto(410,20)
tre.end_fill()

tree=turtle.Turtle()
tree.penup()
tree.speed(0)
tree.goto(-400,-30)
tree.pendown()

tree.begin_fill()
tree.fillcolor('brown')
tree.goto(-400,20)
tree.goto(-410,20)
tree.goto(-410,-30)
tree.end_fill()
tree.hideturtle()
tree.begin_fill()
tree.fillcolor('green')
tree.penup()
tree.goto(-410,20)
tree.pendown()
tree.goto(-420,20)
tree.goto(-420,40)
tree.goto(-390,40)
tree.goto(-390,20)
tree.goto(-410,20)
tree.end_fill()

grass.hideturtle()
dinow.left (90)
dinow.penup()
dinow.goto(0,-16)
grass.color("green")
grass.penup()
grass.goto(0,-25)
grass.begin_fill()
grass.pendown()
grass.goto(-485,-25)
grass.goto(-485,-50)
grass.goto(485,-50)
grass.goto(485,-25)
grass.goto(-485,-25)
grass.end_fill()

def left():
    dinow.setx(dinow.xcor()-30)

def right():
    dinow.setx(dinow.xcor()+30)

def jump():
    global points
    if (points>0):
        dinow.sety(dinow.ycor()+20)
        points=points-1
        score.clear() 
        score.write(f'points: {points}')
 
def spawncoin():
    coin=turtle.Turtle()
    coin.penup()
    x=random.randint(-470,470)
    y=random.randint(0,50)
    coin.color('red')
    coin.goto(x,y)
    return(coin)

coin=spawncoin()

def gravity():
    dinow.sety(dinow.ycor()-1)

def check_border(tr):
    colors=["red","gold","blue","yellow","green"]
    if tr.xcor() > 485:
        tr.speed(0)
        tr.color(random.choice(colors))
        tr.hideturtle()
        tr.setx(-485)
        tr.sety(random.randint(-20,50))
        tr.showturtle()

def reset_coin(coin):
    coin.hideturtle()
    x=random.randint(-470,470)
    y=random.randint(0,50)
    coin.goto(x,y)
    global points
    points+=10
    if (points>0):
        score.clear() 
        score.write(f'points: {points}')
    coin.showturtle()


def coin_border(coin):
    x=coin.xcor()
    y=coin.ycor()
    dino_x=dinow.xcor()
    dino_y=dinow.ycor()
    if(x > (dino_x - 20) and x < (dino_x + 20)):
        if(y >(dino_y -20)and y < (dino_y +20)):
            reset_coin(coin)

def chang_color():
    global points
    global spyd
    if (points>20):
        dinow.color('green')
        spyd=8
    if (points>30):
        dinow.color('blue')
        spyd=11
    if (points>40):
        dinow.color('purple')
        spyd=14
    if (points>50):
        dinow.color('red')
        spyd=16
    if (points>60):
        dinow.color('gold')
        spyd=20
    if (points>70):
        dinow.color('gold')
        spyd=24
    if (points>80):
        dinow.color('gold')
        spyd=28
    if (points>90):
        dinow.color('gold')
        spyd=32
    if (points>100):
        dinow.color('gold')
        spyd=36
    if (points>110):
        dinow.color('gold')
        spyd=40

def check_enemy(t):
    x=dinow.xcor()
    y=dinow.ycor()
    e_x = t.xcor()
    e_y = t.ycor()
    if(x > (e_x - 10) and x < (e_x + 10)):
        if(y >(e_y -10)and y < (e_y +10)):
            global points
            points=points-1000
            if (points<1):
                points=0
            if (points>=0):
                score.clear() 
                score.write(f'points: {points}')

points=10
score=turtle.Turtle()
score.color("black")
score.goto(0,0)
score.hideturtle()
enemies=2
spyd=5

while True:
    gravity()
    window.update()
    window.listen()
    window.onkey(left,"Left")
    window.onkey(right,"Right")
    check_border(dead)
    check_border(dyu)
    coin_border(coin)
    check_enemy(dyu)
    check_enemy(dead)  
    if (dinow.ycor()<-16):
        dinow.sety(-16)
    window.onkey(jump,"space")
    chang_color()
    dead.forward(spyd)
    dyu.forward(spyd)
    if(points>30 and enemies==2):
        dead2=turtle.Turtle()
        dead2.penup()
        enemies=3
    if(enemies==3):
        check_enemy(dead2)
        dead2.forward(spyd)
        check_border(dead2)