import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry('360x340')

'''rButton = Button(root, text='Rock', bg='pink')
rButton.grid(row=1, column=1)

pButton = Button(root, text='Paper', bg= 'blue')
pButton.grid(row=2, column=1)

sButton = Button(root, text='Scissors', bg='green')
sButton.grid(row=3, column=1)'''

RPC = ["Rock", "Paper", "Scissors"]

def buttonFunction(*originalChoice):
    print(*originalChoice)

    aiComputer = random.choice(RPC)

    mylist = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
    nRow, num = 1, 0
    myList2 = ['blue', 'pink', 'green']
    for item in mylist:
        button = Button(root, text=item, command=lambda x=item: buttonFunction(x), bg=myList2[num], height=6, width=45)
        button.grid(row=nRow, column=1)
        nRow+=1
        num+=1

    if originalChoice == ('Rock',) and aiComputer == "Rock":
        messagebox.showinfo("Information","AI:   {} \n User: {} \n It was a tie, try again!".format(aiComputer, *originalChoice))
    elif originalChoice == ('Rock',) and aiComputer == "Paper":
        messagebox.showinfo("Information", "AI:   {} \n User: {} \n AI Wins!".format(aiComputer, *originalChoice))
    elif originalChoice == ('Rock',) and aiComputer == "Scissors":
        messagebox.showinfo("Information", "AI:   {} \n User: {} \n You Win!".format(aiComputer, *originalChoice))
    elif originalChoice == ('Paper',) and aiComputer == "Rock":
        messagebox.showinfo("Information", "AI:   {} \n User: {} \n You Win!".format(aiComputer, *originalChoice))
    elif originalChoice == ('Paper',) and aiComputer == "Paper":
        messagebox.showinfo("Information","AI:   {} \n User: {} \n It was a tie, try again!".format(aiComputer, *originalChoice))
    elif originalChoice == ('Paper',) and aiComputer == "Scissors":
        messagebox.showinfo("Information", "AI:   {} \n User: {} \n AI Wins!".format(aiComputer, *originalChoice))
    elif originalChoice == ('Scissors',) and aiComputer == "Rock":
        messagebox.showinfo("Information", "AI:   {} \n User: {} \n AI Wins!".format(aiComputer, *originalChoice))
    elif originalChoice == ('Scissors',) and aiComputer == "Paper":
        messagebox.showinfo("Information", "AI:   {} \n User: {} \n You Win!".format(aiComputer, *originalChoice))
    elif originalChoice == ('Scissors',) and aiComputer == "Scissors":
        messagebox.showinfo("Information","AI:   {} \n User: {} \n It was a tie, try again!".format(aiComputer, *originalChoice))



buttonFunction()


root.mainloop()