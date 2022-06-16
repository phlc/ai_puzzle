from tkinter import *
import puzzle_ai as ai
import time



###### Local Class ######

class _Button_:
    
    def __init__(self, value, lin, col):
        self.value = value
        self.lin = lin
        self.col = col
        self.number = Button(puzzle_frame, text = " " if self.value==9 else str(self.value), font=('arial', 80), bd=3) 
        self.number.place(x = self.col*150+40, y = self.lin*130+20, width=150, height=130)



###### Widgets ######

# Root
root = Tk()
root.geometry("1350x850+0+0")
root.title("AI Puzzle Game")
root.configure(bg="Cadet Blue")

# Title
top_frame = Frame(root, bg="Cadet Blue", pady=2, width=1350, height=100, relief='ridge')
top_frame.grid(row=0, column=0)
title = Label(top_frame, font=('arial', 80, 'bold'), text="AI Puzzle Game", bd=10, bg="Cadet Blue", 
                                justify=CENTER, fg="Yellow")
title.grid(row=0, column=0)

# Main Frame
main_frame = Frame(root, bg="Powder Blue", bd=10, width=1350, height=500, relief='ridge')
main_frame.grid(row=1, column=0, padx=30)


# Puzzle Fram
puzzle_frame = Frame(main_frame, bd=10, relief="ridge", pady=6, bg="Cadet Blue", width=700, height=600, )
puzzle_frame.pack(side=LEFT)

def show_numbers(numbers):
    for lin in range(len(numbers)):
        for col in range(len(numbers[0])):
            _Button_(numbers[lin][col], lin, col)


# Buttons Frame
buttons_frame = Frame(main_frame, relief="ridge", bg="Cadet Blue", width=540, height=500, bd=10, padx=1, pady=2)
buttons_frame.pack(side=RIGHT)


# Display
moves_time_frame = Frame(buttons_frame, bg="Cadet Blue", bd=10, width=560, height=200, padx=10, pady=0, relief='ridge')
moves_time_frame.grid(row=0, column=0)
moves_counter = 0
time_seconds = '0.0000'
display_moves_time = StringVar()

moves_time_label = Label(moves_time_frame, textvariable=display_moves_time, font=('arial', 40))
moves_time_label.place(x=0, y=10, width=520, height=150)

def update_moves_time(new_moves=0, new_time='0.0000'):
    global moves_counter, time_seconds, display_moves_time
    moves_counter = new_moves
    time_seconds = new_time
    display_moves_time.set(f"Moves:        Time to Solve:    \n{moves_counter}                  {time_seconds}     ")


# Algorithms Frame
algorithm_frame = Frame(buttons_frame, bg="Cadet Blue", bd=10, width=540, height=200, padx=10, pady=2, relief='ridge')
algorithm_frame.grid(row=1, column=0)
algorithm_control = IntVar()

Radiobutton(algorithm_frame, font=('arial', 30), text="      A *       ", indicatoron = 0, height=2,
                  variable=algorithm_control, value=0, pady=10).pack(side="left")
Radiobutton(algorithm_frame, font=('arial', 30), text="   Largura    ", indicatoron = 0, height=2,
                  variable=algorithm_control, value=1, pady=10).pack(side="left")
Radiobutton(algorithm_frame, font=('arial', 30), text="Profundidade ", indicatoron = 0, height=2,
                  variable=algorithm_control, value=2, pady=10).pack(side="left")


# New Game - Reset Frame
reset_new_frame = Frame(buttons_frame, bg="Cadet Blue", bd=10, width=540, height=200, padx=10, pady=2, relief='ridge')
reset_new_frame.grid(row=2, column=0)
def reset_game():
    update_moves_time()
    show_numbers(ai.reset_game())

def new_game():
    update_moves_time()
    show_numbers(ai.new_game())

def solve():
    initial_time = time.time()
    states_list = ai.solve(algorithm_control.get())
    time_spent = time.time() - initial_time
    moves = 0
    last = len(states_list)-1
    print(last)
    last = 1 if algorithm_control.get() == 2 else last
    while(last!=0):
        root.update()
        time.sleep(0.5)
        show_numbers(states_list[last].board)
        update_moves_time(moves, "{:.4f}".format(time_spent))
        moves += 1
        last -= 1

Button(reset_new_frame, text = "   Reset   \nGame", font=('arial', 30),pady=10, height=2, command=reset_game).pack(side="left")
Button(reset_new_frame, text = "New Game", font=('arial', 30),pady=10, height=2, command=new_game).pack(side="left")
Button(reset_new_frame, text = "   Solve   ", font=('arial', 30),pady=10, height=2, command=solve).pack(side="left")



###### Main Loop ######
new_game()
root.mainloop()