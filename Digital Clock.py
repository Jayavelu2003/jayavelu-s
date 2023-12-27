from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("DIGITAL CLOCK")


def time():
    string = strftime('%H:%M:%S:%p\n%D:%A')
    label.config(text=string)
    label.after(5000, root.destroy)
label = Label(root , font=("arial", 50))
label.pack(side='bottom')
time()
mainloop()
