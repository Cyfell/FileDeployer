import tkinter as tk


class Model:
    def __init__(self):
        self.val = tk.IntVar(0)
        self.server_list = []
        self.server_list_var = tk.StringVar(value=self.server_list)

    def add_one(self):
        self.val.set(self.val.get() + 1)

    def reset(self):
        self.val.set(0)
