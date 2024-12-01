import tkinter

from Algorithm.knight_tour_alg import run_algo
from tkinter import *

def main():
    #CITATION: https://www.geeksforgeeks.org/python-gui-tkinter/#
    master = Tk()
    master.title('Knight Tour')
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
    center_and_top(master)
    mainloop()

def on_click(e1text, e2text, master, label_inv):
    if not run_algo(int(e1text), int(e2text)):
        label_inv.grid(row=3, column=0)
    else:
        label_inv.grid_forget()

def center_and_top(window):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()


    width = window.winfo_width()
    height = window.winfo_height()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{700}x{500}+{x - height}+{y - width}")
    window.lift()
    window.focus_force()

if __name__ == "__main__":
    main()