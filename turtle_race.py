import turtle
from tkinter import *
import time
import random

WIDTH,HEIGHT=500,500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racers=0
    while True:
        racers=input('Enter the number of racers (2-10): ')
        if racers.isdigit():
            racers=int(racers)
            if 2<=racers<=10:
                return racers
            else:
                print('Number not in range 2-10. Try Again!')
        else:
            print('Input is not numeric... Try Again!')
            continue

def init_turtle(canvas):
    screen=turtle.TurtleScreen(canvas)
    # screen.title('Turtle Racing')
    return screen

def race(colors,canvas):
    turtles=create_turtles(colors,canvas)

    while True:
        for racer in turtles:
            distance=random.randint(1,20)
            racer.pendown()
            racer.forward(distance)
            x,y=racer.pos()
            if y>=HEIGHT//2-10:
                return colors[turtles.index(racer)]


def create_turtles(colors,canvas):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer=turtle.RawTurtle(canvas)
        racer.shape('turtle')
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingx,-HEIGHT//2+20)
        turtles.append(racer)
    
    return turtles

racers=get_number_of_racers()
root=Tk()
canvas=turtle.ScrolledCanvas(root,WIDTH,HEIGHT)
canvas.pack()
root.title("Turtle Race...")
screen=init_turtle(canvas)
random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors,canvas)
time.sleep(0.7)
screen.clearscreen()

winner_racer=turtle.RawTurtle(canvas)
winner_racer.shape('turtle')
winner_racer.color(winner)
winner_racer.penup()
winner_racer.setpos(0,-50)

congratsQuote=turtle.RawTurtle(canvas)
congratsQuote.color(winner)
congratsQuote.hideturtle()
congratsQuote.write(f'The winner is {winner}',align="center",font=('Arial', 24, 'normal'))

while root:
    winner_racer.left(90)

root.mainloop()

print(f'The winner is {winner}')

