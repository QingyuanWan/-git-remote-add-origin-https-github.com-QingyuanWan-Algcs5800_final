import tkinter

from Algorithm.knight_tour_alg import run_algo
from tkinter import *

def main():
    #CITATION: https://www.geeksforgeeks.org/python-gui-tkinter/#
    master = Tk()
    labelRow = Label(master, text='number of rows')
    labelRow.grid(row=0, column = 0)
    LabelColumn = Label(master, text='number of columns')
    LabelColumn.grid(row=1, column=0)
    label_inv = Label(master, text="invalid board, try again.")

    e1 = Entry(master)
    e2 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


    button = Button(master, text="Show Tour!", command=lambda: on_click(e1.get(), e2.get(), master, label_inv))
    button.grid(row=2, column = 0)
    mainloop()

def on_click(e1text, e2text, master, label_inv):
    if not run_algo(int(e1text), int(e2text)):
        label_inv.grid(row=3, column=0)
    else:
        label_inv.grid_forget()


if __name__ == "__main__":
    main()