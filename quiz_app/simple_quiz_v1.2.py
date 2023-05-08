import tkinter as tk
from tkinter import StringVar, ttk
from PIL import ImageTk, Image


root = tk.Tk()
root.geometry('500x500')

frame = tk.Frame(root, padx=10, pady=10, bg="#fff")
frame.configure(highlightbackground="#333", highlightthickness=2)

question_label = tk.Label(frame, height=5, width=28, bg="gray", fg="#fff", font=("Arial", 20), wraplength=500)
question_label.configure(highlightbackground="#333", highlightthickness=2, padx=10, pady=10, anchor="center")

progress_label = tk.Label(root, text="0% complete", font=("Arial", 14))
progress_label.pack()

style = ttk.Style()
style.configure("TRadiobutton", background="#fff", font=("Arial", 20), foreground="#333")

questions = ["1 + 1 = ?", "2 + 2 = ?", "3 + 3 = ?", "4 + 4 = ?", "5 + 5 = ?"]
options = [["A", "B", "2", "C", "2"], ["A", "4", "V", "C", "4"],
           ["A", "B", "Z", "6", "6"], ["8", "B", "D", "C", "8"], ["D", "10", "A", "C", "10"]]


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = ttk.Radiobutton(frame, variable=v1, text="Option 1", style="TRadiobutton",
                          command=lambda: checkanswer(option1))
option2 = ttk.Radiobutton(frame, variable=v2, text="Option 2", style="TRadiobutton",
                          command=lambda: checkanswer(option2))
option3 = ttk.Radiobutton(frame, variable=v3, text="Option 3", style="TRadiobutton",
                          command=lambda: checkanswer(option3))
option4 = ttk.Radiobutton(frame, variable=v4, text="Option 4", style="TRadiobutton",
                          command=lambda: checkanswer(option4))

button_next = tk.Button(frame, text="NEXT ", bg="orange", font=("Arial", 20), command=lambda: displaynextquestion())

next_icon = Image.open("next.png")
next_icon = next_icon.resize((60, 50), Image.LANCZOS)

next_image = ImageTk.PhotoImage(next_icon)

button_next.config(image=next_image, compound="right")

frame.pack(fill="both", expand=True)

question_label.grid(row=0, column=0)

option1.grid(sticky="W", row=1, column=0)
option2.grid(sticky="W", row=2, column=0)
option3.grid(sticky="W", row=3, column=0)
option4.grid(sticky="W", row=4, column=0)

button_next.grid(row=6, column=0)

correct = 0
index = 0
current_question = 0


def disablebuttons(state):

    option1["state"] = state
    option2["state"] = state
    option3["state"] = state
    option4["state"] = state


def checkanswer(radio):
    global correct, index

    if radio['text'] == options[index][4]:
        correct += 1

    index += 1
    disablebuttons('disable')


def update_progress_label():
    global current_question

    progress_percent = (current_question / len(questions)) * 100
    progress_label.config(text=f"{progress_percent:.0f}% complete")
    current_question += 1


def displaynextquestion():
    global correct, index, current_question

    if button_next['text'] == "Restart The Quiz ":
        correct = 0
        index = 0
        current_question = 0
        question_label['bg'] = "gray"
        button_next['text'] = "NEXT "

    if index == len(options):
        question_label['text'] = str(correct) + "/" + str(len(options))
        button_next['text'] = "Restart The Quiz "

        if correct >= len(options)/2:
            question_label['bg'] = "green"
        else:
            question_label['bg'] = "red"

    update_progress_label()

    question_label['text'] = questions[index]

    disablebuttons('normal')

    opts = options[index]

    option1['text'] = opts[0]
    option2['text'] = opts[1]
    option3['text'] = opts[2]
    option4['text'] = opts[3]

    v1.set(opts[0])
    v2.set(opts[1])
    v3.set(opts[2])
    v4.set(opts[3])


displaynextquestion()

root.mainloop()
