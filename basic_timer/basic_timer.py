from tkinter import *
from playsound import playsound
import time
from PIL import Image, ImageTk

root = Tk()
root.title("Basic Timer")
root.geometry("400x600")
root.config(bg="black")
root.resizable(False, False)

head_title = Label(root, text="Timer", font="Arial 30 bold", bg="black", fg="red")
head_title.pack(pady=10)

Label(root, font=("Arial", 15, "bold"), text="Current time:", background="white").place(x=65, y=70)


def clock():

    clock_time = time.strftime("%H:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font=("Arial", 15, "bold"), text="", fg="black", bg="white")
current_time.place(x=190, y=70)
clock()

hours = StringVar()
Entry(root, textvariable=hours, font="Arial 50", width=2, bg="black", fg="yellow", bd=0).place(x=30, y=155)
hours.set("00")

mins = StringVar()
Entry(root, textvariable=mins, font="Arial 50", width=2, bg="black", fg="yellow", bd=0).place(x=150, y=155)
mins.set("00")

sec = StringVar()
Entry(root, textvariable=sec, font="Arial 50", width=2, bg="black", fg="yellow", bd=0).place(x=270, y=155)
sec.set("00")

Label(root, text="Hours", font="Arial 12", bg="black", fg="white").place(x=105, y=200)
Label(root, text="Min", font="Arial 12", bg="black", fg="white").place(x=225, y=200)
Label(root, text="Sec", font="Arial 12", bg="black", fg="white").place(x=345, y=200)


def timer():

    times = int(hours.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())

    while times > -1:
        minute, second = (times // 60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set(str(second))
        mins.set(str(minute))
        hours.set(str(hour))

        root.update()
        time.sleep(1)

        if times == 0:
            playsound("alarm.wav")
            sec.set("00")
            mins.set("00")
            hours.set("00")

        times -= 1


def train_command():

    hours.set("01")
    mins.set("00")
    sec.set("00")


def run_command():
    hours.set("00")
    mins.set("40")
    sec.set("00")


def rest_command():
    hours.set("00")
    mins.set("02")
    sec.set("00")


btn = Button(root, text="START", font="Arial 10 bold", bg="red", fg="white", bd=0, width=20, height=2, command=timer)
btn.pack(padx=5, pady=40, side="bottom")

training = Image.open("training.png")
training = training.resize((127, 127), Image.LANCZOS)
image_training = ImageTk.PhotoImage(training)
btn_training = Button(root, image=image_training, bg="white", bd=0, command=train_command)
btn_training.place(x=7, y=300)


running = Image.open("running.png")
running = running.resize((127, 127), Image.LANCZOS)
image_running = ImageTk.PhotoImage(running)
btn_running = Button(root, image=image_running, bg="white", bd=0, command=run_command)
btn_running.place(x=137, y=300)

resting = Image.open("resting.png")
resting = resting.resize((127, 127), Image.LANCZOS)
image_resting = ImageTk.PhotoImage(resting)
btn_resting = Button(root, image=image_resting, bg="white", bd=0, command=rest_command)
btn_resting.place(x=267, y=300)

Label(root, text="Train", font="Arial 12", bg="black", fg="white").place(x=52, y=430)
Label(root, text="Run", font="Arial 12", bg="black", fg="white").place(x=187, y=430)
Label(root, text="Rest", font="Arial 12", bg="black", fg="white").place(x=312, y=430)

root.mainloop()
