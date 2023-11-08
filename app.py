import math
import random
from tkinter import *

root = Tk()
root.title("Think of a number")
root.geometry("400x300")

startmin = IntVar()
startmax = IntVar()
min = 1
max = 100
ready = False
n = 0

Spinbox(root, from_ = 1, to = 999999999998, textvariable = startmin).grid(column = 1, row = 1, padx = 10, pady = 30)
Spinbox(root, from_ = 100, to = 999999999999, textvariable = startmax).grid(column = 3, row = 1, padx = 10, pady = 30)
l = Label(root, text = int(n))

def calc():
    global n
    if (((min + max) % 2) != 0):
        n = int(random.randint(math.floor(((min + max) / 2)), math.ceil(((min + max) / 2))))
    else:
        n = int((min + max) / 2)
    
def lower():
    global max
    max = int(n - 1)
    calc()
    l.grid_forget()
    Label(root, text = int(n)).grid(column = 2, row = 2, padx = 10, pady = 30)

def higher():
    global min
    min = int(n + 1)
    calc()
    l.grid_forget()
    Label(root, text = int(n)).grid(column = 2, row = 2, padx = 10, pady = 30)

def start():
    global ready
    global min
    global max
    if ready == False:
        min = startmin.get()
        max = startmax.get()
        calc()
        l = Label(root, text = int(n))
        l.grid(column = 2, row = 2, padx = 10, pady = 30)
        ready = True

def done():
    root.destroy()

Button(root, text = "Lower", command = lower).grid(column = 1, row = 3, padx = 10, pady = 30)
Button(root, text = "Start", command = start).grid(column = 2, row = 1, padx = 10, pady = 30)
Button(root, text = "OK", command = done).grid(column = 2, row = 3, padx = 10, pady = 30)
Button(root, text = "Higher", command = higher).grid(column = 3, row = 3, padx = 10, pady = 30)

root.mainloop()