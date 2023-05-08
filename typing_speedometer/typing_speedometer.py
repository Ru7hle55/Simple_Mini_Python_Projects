import tkinter as tk
import time
import threading
import random


class TypeSpeedGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing speedometer")
        self.root.geometry("800x560")
        self.root.config(bg="black")

        self.texts = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.counter = 0
        self.running = False

        self.timer_label = tk.Label(self.frame, text=f"{self.counter:.1f} Seconds", font=("Helvetica", 24), fg="red")
        self.timer_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Helvetica", 18))
        self.sample_label.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        self.characters = len(self.sample_label.cget('text'))
        self.words = len(self.sample_label.cget('text').split(' '))
        self.char_index = 0
        self.word_index = 0

        self.sample_info_label = tk.Label(self.frame, text=f"{len(self.sample_label.cget('text'))} Characters left"
                                                           f"\n{len(self.sample_label.cget('text').split(' '))} "
                                                           f"Words left")
        self.sample_info_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(self.frame, text=f"Speed: \n0.00 Characters Per Second\n0.00 Characters Per Minute"
                                                     "\n0.00 Words Per Second\n0.00 Words Per Minute",
                                                     font=("Helvetica", 18))
        self.speed_label.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=("Helvetica", 24))
        self.reset_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.root.mainloop()

    def timer(self):
        self.timer_label.config(text=f"{self.counter:.1f} Seconds")

    def sample_info(self):
        try:
            if self.sample_label.cget('text')[self.char_index] == self.input_entry.get()[self.char_index]:
                if len(self.sample_label.cget('text').split(' ')[self.word_index]) == \
                        len(self.input_entry.get().split(' ')[self.word_index]):
                    self.words -= 1
                    self.word_index += 1

                self.characters -= 1
                self.char_index += 1
                self.sample_info_label.config(text=f"{self.characters} Characters left\n{self.words} Words left")

        except IndexError:
            ...

    def start(self, event):
        if not self.running:
            if event.keycode not in [16, 17, 18, 8, 32]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()

        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            self.sample_info()
            self.timer()
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} Characters Per Second\n{cpm:.2f} Characters Per Minute"
                                         f"\n{wps:.2f} Words Per Second\n{wpm:.2f} Words Per Minute")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 Characters Per Second\n0.00 Characters Per Minute\n0.00 Words Per"
                                     " Second\n0.00 Words Per Minute")
        self.sample_label.config(text=random.choice(self.texts))
        self.sample_info_label.config(text=f"{len(self.sample_label.cget('text'))} Characters left"
                                           f"\n{len(self.sample_label.cget('text').split(' '))} Words left")
        self.input_entry.delete(0, tk.END)
        self.timer()


TypeSpeedGUI()
