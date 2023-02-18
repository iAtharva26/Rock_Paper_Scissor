from  tkinter import *
from random import randint
from PIL import Image,ImageTk
from sketchpy import library as li

root=Tk()
root.title("ROCK")
root.configure(bg="purple")

rockimag=ImageTk.PhotoImage(Image.open("rock1.png"))
paperimag=ImageTk.PhotoImage(Image.open("paper(paper).png"))
scissorsimag=ImageTk.PhotoImage(Image.open("scissors_(scissors).png"))

rock2=ImageTk.PhotoImage(Image.open("rock2.png"))
paper2=ImageTk.PhotoImage(Image.open("paper2.png"))
scissors2=ImageTk.PhotoImage(Image.open("scissors_(scissors) 2 (1).png"))

userlabel=Label(root,image=scissorsimag,bg="purple")
comlabel=Label(root,image=rock2,bg="purple")
comlabel.grid(row=1,column=0)
userlabel.grid(row=1,column=4)

playersco=Label(root,text=0,font=100,bg="purple",fg="white")
comsco=Label(root,text=0,font=100,bg="purple",fg="white")
comsco.grid(row=1,column=1)
playersco.grid(row=1,column=3)

user_indicators=Label(root,font=62,text="USER",bg="purple",fg="white").grid(row=0,column=3)
comp_indicators=Label(root,font=62,text="COMPUTER",bg="purple",fg="white").grid(row=0,column=1)

msg=Label(root,font=30,bg="purple",fg="white")
msg.grid(row=8,column=2,)

def updatemsg(x):
    msg['text'] = x

def scoreuupdate():
    score = int(playersco['text'])
    score += 1
    playersco['text'] = str(score)

def scorecupdate():
    score = int(comsco['text'])
    score += 1
    comsco["text"] = str(score)

def winner(player,computer):
    if player == computer:
        updatemsg("!!!---TIE---!!!")
    elif player == "rock":
        if computer == "paper":
            updatemsg("WINNER COMPUTER")
            scorecupdate()
        else:
            updatemsg("WINNER USER")
            scoreuupdate()
    elif player == "paper":
        if computer == "scissor":
            updatemsg("WINNER COMPUTER")
            scorecupdate()
        else:
            updatemsg("WINNER USER")
            scoreuupdate()
    elif player == "scissor":
        if computer == "rock":
            updatemsg("WINNER COMPUTER")
            scorecupdate()
        else:
            updatemsg("WINNER USER")
            scoreuupdate()

comchoice=["rock","paper","scissor",]

def choice(x):

    comChoice=comchoice[randint(0,2)]
    if comChoice == "rock":
        comlabel.configure(image=rockimag)
    elif comChoice == "paper":
        comlabel.configure(image=paperimag)
    else:
        comlabel.configure(image=scissorsimag)

    if x == "rock":
        userlabel.configure(image=rockimag)
    elif x == "paper":
        userlabel.configure(image=paperimag)
    else:
        userlabel.configure(image=scissorsimag)


    winner(x,comChoice)

rock=Button(root,width=20,height=2,text="ROCK",bg="RED",fg="white",command=lambda:choice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="GREEN",fg="white",command=lambda:choice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="Orange",fg="white",command=lambda:choice("scissor")).grid(row=2,column=3)

root.mainloop()