from tkinter import *
from math import *

root = Tk()

root.title("Compound Interest Calculator By @SmashdFrenzy16")

princ = Entry(root, width=100, borderwidth=5)
princ.pack()
princ.insert(0, "Enter Principle Amount")
rate = Entry(root, width=100, borderwidth=5)
rate.pack()
rate.insert(0, "Enter Rate")
time = Entry(root, width=100, borderwidth=5)
time.pack()
time.insert(0, "Enter Time")

def compound_interest():


    amount = float(princ.get())*(1+(float(rate.get())/100))**time()

    ci = amount - float(princ.get())

    print(ci)

enter = Button(root, text="Enter", command=compound_interest)
enter.pack()

root.mainloop()