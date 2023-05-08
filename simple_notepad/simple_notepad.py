import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import os


def create_notepad():

    global textfield
    textfield = Text(root)
    textfield.grid(sticky=N+W+E+S)

    menubar = Menu(root)
    root.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New File", command=create_new_file)
    filemenu.add_command(label="Open File", command=open_file)
    filemenu.add_command(label="Save File", command=save_file)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_file)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=cut_text)
    editmenu.add_command(label="Copy", command=copy_text)
    editmenu.add_command(label="Paste", command=paste_text)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About Simple Notepad", command=help_menu)
    menubar.add_cascade(label="Help", menu=helpmenu)


def create_new_file():

    global textfield
    root.title("Simple Notepad")
    file = None
    textfield.delete(1.0, END)


def open_file():

    global textfield

    file = filedialog.askopenfile(defaultextension=".txt",
                                  filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
    file = file.name

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Simple Notepad.txt")
        textfield.delete(1.0, END)
        file = open(file, "r")
        textfield.insert(1.0, file.read())
        file.close()


def save_file():

    global textfield, file

    if file is None:
        file = filedialog.asksaveasfilename(initialfile="Simple Notepad.txt", defaultextension=".txt",
                                            filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if file is None:
            file = None
        else:
            file = open(file, "w")
            file.write(textfield.get(1.0, END))
            file.close()
            file = file.name
            root.title(os.path.basename(file) + " - Simple Notepad")

    else:
        file = open(file, "w")
        file.write(textfield.get(1.0, END))
        file.close()


def exit_file():

    root.destroy()


def cut_text():

    global textfield
    textfield.event_generate("<<Cut>>")


def copy_text():

    global textfield
    textfield.event_generate("<<Copy>>")


def paste_text():

    global textfield
    textfield.event_generate("<<Paste>>")


def help_menu():

    messagebox.showinfo("Simple Notepad", "This is a simple notepad editor that can be used to edit text")


root = tk.Tk()
root.title("SIMPLE NOTEPAD")
file = None

create_notepad()
root.mainloop()
