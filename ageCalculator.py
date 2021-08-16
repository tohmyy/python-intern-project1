import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.geometry("330x470")
root.title("Age Calculator")

Label(root, text="Name").grid(row=2, column=1)
nameEntry = Entry(root)
nameEntry.grid(row=2, column=2)

Label(root, text="Year").grid(row=3, column=1)
yearEntry = Entry(root)
yearEntry.grid(row=3, column=2)

Label(root, text="Month").grid(row=4, column=1)
monthEntry = Entry(root)
monthEntry.grid(row=4, column=2)

Label(root, text="Date").grid(row=5, column=1)
dateEntry = Entry(root)
dateEntry.grid(row=5, column=2)

def getInput():
    name = nameEntry.get()
    geForce = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
    messagebox.showinfo("Information","Heyy {geForce}!!!. You are {age} years old!!!".format(geForce=name, age= geForce.age()))

button = Button(root, text="Calculate Your Age", command=getInput, bg="pink")
button.grid(row=6, column=2, sticky=E)

class Person:
    def __init__(self, name, birthDate):
        self.name = name
        self.birthDate = birthDate
    def age(self):
        todayDate = datetime.date.today()

        age = todayDate.year-self.birthDate.year
        return age

image1 = Image.open('images (30).jpeg')
image1.thumbnail((300, 300), Image.ANTIALIAS)

picture = ImageTk.PhotoImage(image1)
label_image = Label(root, image=picture)
label_image.grid(row=0, column=2)

root.mainloop()