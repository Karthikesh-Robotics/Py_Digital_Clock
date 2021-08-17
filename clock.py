from tkinter import *
import time


def digital():
    t = time.strftime("%H:%M:%S")
    clock.config(text=t)
    clock.after(500, digital)


root = Tk()
root.title = 'Digital Clock'
clock = Label(root, font=('times', 50, 'bold'), bg='red')
clock.grid(row=1, column=0, )
digital()
root.mainloop()

