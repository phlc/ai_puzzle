import random
from tkinter import E


# Define Solution
_SOLUTION_ = []
value = 1
for lin in range(4):
    line = [] 
    for col in range(4):
        line.append(value)
        value += 1
    _SOLUTION_.append(line)



# New Puzzle
def _shuffle_():
    base = list(range(1,17))
    random.shuffle(base)
    new_numbers = []
    for i in range(4):
        line = []
        for j in range(4):
            line.append(base[4*i + j])
        new_numbers.append(line)    
    return new_numbers

# state = board + parent
class _state_:
    def __init__(self, board, parent):
        self.board = board
        self.parent = parent


_initial_state_ = None
_states_list_ = []


# Local Functions
def equals(a, b):
    for i in range(4):
        for j in range(4):
            if(a[i][j] != b[i][j]):
                return False
    return True

def is_solution(a):
    return equals(_SOLUTION_, a)

def list_contains(a):
    for state in _states_list_:
        if(equals(a, state.board)):
            return True
    return False

def empty_pos(a):
    for lin in range(4):
        for col in range(4):
            if(a[lin][col] == 16):
                return (lin, col)
    return None

def _a_star_():
    pass


def _breadth_search_():
    pass


def _deep_search_():
    pass

# Interface Functions
def new_game():
    global _initial_state_, _states_list_
    _states_list_ = []
    _initial_state_ = _state_(_shuffle_(), 0)
    _states_list_.append(_initial_state_)
    return _states_list_[0].board  


def reset_game():
    global _initial_state_, _states_list_
    _states_list_ = []
    _states_list_.append(_initial_state_)
    return _states_list_[0].board


def solve(x):
    if(x==0):
        return _a_star_()
    elif(x==1):
        return _breadth_search_()
    elif(x==2):
        return _deep_search_()
    else:
        return []
