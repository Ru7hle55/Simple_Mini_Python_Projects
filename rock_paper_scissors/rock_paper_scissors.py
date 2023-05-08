from tkinter import *
from random import randint
from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x600")
root.resizable(False, False)
root.config(bg="white")

rock = Image.open("rock.png")
paper = Image.open("paper.png")
scissors = Image.open("scissors.png")

rock = rock.resize((300, 300), Image.LANCZOS)
paper = paper.resize((300, 300), Image.LANCZOS)
scissors = scissors.resize((300, 300), Image.LANCZOS)

rock = ImageTk.PhotoImage(rock)
paper = ImageTk.PhotoImage(paper)
scissors = ImageTk.PhotoImage(scissors)

images = [rock, paper, scissors]

random_number = randint(0, 2)

image_label = Label(root, image=images[random_number], bd=0)
image_label.pack(pady=20)


def spin():

    random_number = randint(0, 2)
    image_label.config(image=images[random_number])

    if choose_item.get() == "Rock":
        choose_item_value = 0
    elif choose_item.get() == "Paper":
        choose_item_value = 1
    elif choose_item.get() == "Scissors":
        choose_item_value = 2

    if choose_item_value == 0:
        if random_number == 0:
            win_loose_label.config(text="IT IS A TIE ! SPIN AGAIN !", bg="yellow")
        elif random_number == 1:
            win_loose_label.config(text="PAPER COVERS ROCK ! YOU LOSE !", bg="red")
        elif random_number == 2:
            win_loose_label.config(text="ROCK SMASHES SCISSORS ! YOU WIN !", bg="green")

    if choose_item_value == 1:
        if random_number == 1:
            win_loose_label.config(text="IT IS A TIE ! SPIN AGAIN !", bg="yellow")
        elif random_number == 0:
            win_loose_label.config(text="PAPER COVER ROCK ! YOU WIN !", bg="green")
        elif random_number == 2:
            win_loose_label.config(text="SCISSORS CUTS PAPER ! YOU LOSE !", bg="red")

    if choose_item_value == 2:
        if random_number == 2:
            win_loose_label.config(text="IT IS A TIE ! SPIN AGAIN !", bg="yellow")
        elif random_number == 1:
            win_loose_label.config(text="SCISSORS CUTS PAPER ! YOU WIN !", bg="green")
        elif random_number == 0:
            win_loose_label.config(text="ROCK SMASHES SCISSORS ! YOU LOSE !", bg="red")


choose_item = ttk.Combobox(root, values=("Rock", "Paper", "Scissors"))
choose_item.current(0)
choose_item.pack(pady=20)

button_spin = Button(root, text="SPIN NOW !", command=spin)
button_spin.pack(pady=10)

win_loose_label = Label(root, text="", font=("Helvetica", 18), bg="white")
win_loose_label.pack(pady=50)

root.mainloop()
