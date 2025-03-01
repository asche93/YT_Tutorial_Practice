"""
Title: TTKBootstrap: Easiest Way To Build Modern GUIs in Python
Source: NeuralNine YouTube Channel
Author (Original Tutorial): NeuralNine
URL: https://www.youtube.com/watch?v=aAk3ORDr63U
Date of Implementation: 2025-03-01
Description:
    In this video we learn how to easily build modern graphical user interface (GUI) applications
    in Python with TTKBootstrap.
    Source code: https://github.com/NeuralNine/youtube-tutorials/tree/main/TTKBootstrap

How to make a simple GUI.
"""

import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap import Style

root = tk.Tk()

style = Style(theme="darkly")
root.title("Gui")
root.geometry("300x200")

button1 = ttk.Button(root, text="Button 1", bootstyle="info")
button1.pack()

button2 = ttk.Button(root, text="Button 2", bootstyle="success")
button2.pack()

button3 = ttk.Button(root, text="Button 3", bootstyle="warning")
button3.pack()

root.mainloop()
