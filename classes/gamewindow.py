import tkinter as tk
from tkinter import ttk

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Troll Slayer")
        self.geometry("600x400")

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(pady=20)

        self.text_widget = tk.Text(self.main_frame, wrap=tk.WORD, width=60, height=15)
        self.text_widget.pack()

        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=10)

        self.entry = ttk.Entry(self.input_frame, width=30)
        self.entry.pack(side=tk.LEFT)
        self.entry.bind('<Return>', lambda event: self.process_input())

        self.submit_button = ttk.Button(self.input_frame, text="Submit", command=self.process_input)
        self.submit_button.pack(side=tk.LEFT)

        self.current_input = ""

    def process_input(self):
        self.current_input = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)
        self.text_widget.update()

    def read(self):
        self.current_input = ""
        while not self.current_input:
            self.update()
        return self.current_input