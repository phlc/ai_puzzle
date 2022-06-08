from tkinter import *
import random
import tkinter.messagebox
import time

from scipy import rand

root = Tk()
root.geometry("1350x850+0+0")
root.title("AI Puzzle Game")
root.configure(bg="Cadet Blue")

top_frame = Frame(root, bg="Cadet Blue", pady=2, width=1350, height=100, relief='ridge')
top_frame.grid(row=0, column=0)

title = Label(top_frame, font=('arial', 80, 'bold'), text="AI Puzzle Game", bd=10, bg="Cadet Blue", 
                                justify=CENTER, fg="Yellow")
title.grid(row=0, column=0)

main_frame = Frame(root, bg="Powder Blue", bd=10, width=1350, height=500, relief='ridge')
main_frame.grid(row=1, column=0, padx=30)

puzzle_frame = Frame(main_frame, bd=10, relief="ridge", pady=6, bg="Cadet Blue", width=700, height=600, )
puzzle_frame.pack(side=LEFT)

buttons_frame = Frame(main_frame, relief="ridge", bg="Cadet Blue", width=540, height=500, bd=10, padx=1, pady=2)
buttons_frame.pack(side=RIGHT)

moves_time_frame = Frame(buttons_frame, bg="Cadet Blue", bd=10, width=540, height=200, padx=10, pady=2, relief='ridge')
moves_time_frame.grid(row=0, column=0)

algorithm_frame = Frame(buttons_frame, bg="Cadet Blue", bd=10, width=540, height=200, padx=10, pady=2, relief='ridge')
algorithm_frame.grid(row=1, column=0)

reset_new_frame = Frame(buttons_frame, bg="Cadet Blue", bd=10, width=540, height=200, padx=10, pady=2, relief='ridge')
reset_new_frame.grid(row=2, column=0)

moves_counter = 0
time_seconds = 0
display_moves_time = StringVar()
display_moves_time.set(f"Moves:             Time:    \n{moves_counter}                      {time_seconds}")


def update_moves_time():
    global moves_counter, time_seconds, display_moves_time
    display_moves_time.set(f"Moves:             Time:    \n{moves_counter}                      {time_seconds}")


class Button:
    
    def __init__(self, text, x, y):
        self.value = text
        self.x = x
        self.y = y
        self.number = Button(puzzle_frame, text = self.value, font=('arial', 80), bd=3,
                            command = lambda i=self.x, j=self.j : empty_spot_checker(i, j)) 
        self.number.place(x = self.x*150, y = self.y*150, width=170, height=170)


def shuffle(size):
    numbers = []
    for x in range(size):
        numbers.append(str(x))
    numbers.append("")
    random.shuffle(numbers)
    print(numbers)    


moves_time_label = Label(moves_time_frame, textvariable=display_moves_time, font=('arial', 40))
moves_time_label.place(x=0, y=10, width=480, height=150)

algorithm_control = IntVar()

def test():
    print(algorithm_control.get())

Radiobutton(algorithm_frame, font=('arial', 30), text="      A *      ", indicatoron = 0, height=2,
                  variable=algorithm_control, value=0, command=test, pady=10).pack(side="left")
Radiobutton(algorithm_frame, font=('arial', 30), text="   Largura   ", indicatoron = 0, height=2,
                  variable=algorithm_control, value=1, command=test, pady=10).pack(side="left")
Radiobutton(algorithm_frame, font=('arial', 30), text="Profundidade", indicatoron = 0, height=2,
                  variable=algorithm_control, value=2, command=test, pady=10).pack(side="left")

root.mainloop()