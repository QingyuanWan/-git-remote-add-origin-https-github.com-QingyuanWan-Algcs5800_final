import tkinter as tk
from Algorithm.knight_tour_alg import solve_knights_tour, create_init_table, check_valid, test_print

root= tk.Tk()
root.title("Knight Tour")
root.geometry("700x700")

input_m =tk.StringVar()
input_n =tk.StringVar()


def create_board():

    m_cordin=input_m.get()
    n_cordin=input_n.get()
    
    chess_board = create_init_table(m_cordin, n_cordin)
    

    start_x, start_y = 1, 1
    chess_board[start_x][start_y] = 0
    
    if solve_knights_tour(chess_board, start_x, start_y, 1):
        print("Log: valid graph")
        create_animation(chess_board)
    else:
        print("Log Error: Non valid graph.")
        input_m.set("")
        input_n.set("")





row_label = tk.Label(root, text = 'Input row(m)', font=('calibre',10, 'bold'))
 
m_entry = tk.Entry(root,textvariable = input_m, font=('calibre',10,'normal'))
 
col_label = tk.Label(root, text = 'Input col(n)', font = ('calibre',10,'bold'))
 
n_entry=tk.Entry(root, textvariable = input_n, font = ('calibre',10,'normal'))
 
create_board_btn=tk.Button(root,text = 'Create Board', command = create_board)
 
 
 
row_label.grid(row=0,column=0)
m_entry.grid(row=0,column=1)
col_label.grid(row=1,column=0)
n_entry.grid(row=1,column=1)
create_board_btn.grid(row=2,column=1)

root.mainloop()