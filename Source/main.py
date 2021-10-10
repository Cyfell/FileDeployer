import tkinter as tk
from tkinter import Canvas
from Controller import Controller


if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
