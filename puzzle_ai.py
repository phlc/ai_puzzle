import random


# Define Solution
_SOLUTION_ = []
value = 1
for lin in range(3):
    line = [] 
    for col in range(3):
        line.append(value)
        value += 1
    _SOLUTION_.append(line)



# New Puzzle
def _shuffle_():
    base = list(range(1,10))
    random.shuffle(base)
    empty_pos = (-1, -1)
    new_numbers = []
    for i in range(3):
        line = []
        for j in range(3):
            line.append(base[3*i + j])
            if(base[3*i + j] == 9):
                empty_pos = (i, j)
        new_numbers.append(line)    
    return (empty_pos, new_numbers)


# state = board + parent
class _state_:
    def __init__(self, board, parent, index, empty_pos):
        self.board = board
        self.parent = parent
        self.index = index
        self.empty_pos = empty_pos


# Global Variables
_initial_state_ = None
_solution_pos_ = -1
_solved_ = False
_visited_list_ = []
_path_list_ = []

# Module Functions
def equals(a, b):
    for i in range(3):
        for j in range(3):
            if(a[i][j] != b[i][j]):
                return False
    return True

def is_solution(a):
    return equals(_SOLUTION_, a)

def in_visited(a):
    for state in _visited_list_:
        if(equals(a, state.board)):
            return True
    return False

def copy_board(a):
    new_board = []
    for i in range(3):
        new_line = []
        for j in range(3):
            new_line.append(a[i][j])
        new_board.append(new_line)
    return new_board

def _a_star_():
    pass


def _breadth_search_():
    global _visited_list_, _solution_pos_, _solved_
    
    queue = []
    queue.append(_initial_state_)

    while(not _solved_ and len(queue)>0):
        state = queue.pop(0)
        board = state.board
        print(len(_visited_list_))
        print(board)
        index = state.index
        empty_lin, empty_col = state.empty_pos

        if(not _solved_ and 0 <= empty_lin-1):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin-1][empty_col]
            new_board[empty_lin-1][empty_col] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin-1, empty_col))
                _visited_list_.append(new_state)
                queue.append(new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True
        
        if(not _solved_ and 0<= empty_col-1):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin][empty_col-1]
            new_board[empty_lin][empty_col-1] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin, empty_col-1))
                _visited_list_.append(new_state)
                queue.append(new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True
        
        if(not _solved_ and empty_col+1 < 3):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin][empty_col+1]
            new_board[empty_lin][empty_col+1] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin, empty_col+1))
                _visited_list_.append(new_state)
                queue.append(new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True

        if(not _solved_ and empty_lin+1 < 3):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin+1][empty_col]
            new_board[empty_lin+1][empty_col] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin+1, empty_col))
                _visited_list_.append(new_state)
                queue.append(new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True    


def _deep_search_():
    global _visited_list_, _solution_pos_, _solved_
    
    stack = []
    stack.append(_initial_state_)

    while(not _solved_ and len(stack)>0):
        state = stack.pop()
        board = state.board
        print(len(_visited_list_))
        print(board)
        index = state.index
        empty_lin, empty_col = state.empty_pos

        if(not _solved_ and 0 <= empty_lin-1):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin-1][empty_col]
            new_board[empty_lin-1][empty_col] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin-1, empty_col))
                _visited_list_.append(new_state)
                stack.append(new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True
        
        if(not _solved_ and 0<= empty_col-1):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin][empty_col-1]
            new_board[empty_lin][empty_col-1] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin, empty_col-1))
                _visited_list_.append(new_state)
                stack.append(new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True
        
        if(not _solved_ and empty_col+1 < 3):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin][empty_col+1]
            new_board[empty_lin][empty_col+1] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin, empty_col+1))
                _visited_list_.append(new_state)
                stack.append(new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True

        if(not _solved_ and empty_lin+1 < 3):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin+1][empty_col]
            new_board[empty_lin+1][empty_col] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin+1, empty_col))
                _visited_list_.append(new_state)
                stack.append(new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True    



# Interface Functions
def new_game():
    global _visited_list_, _initial_state_, _path_list_, _solved_, _solution_pos_
    _visited_list_ = []
    _path_list_ = []
    _solved_ = False
    _solution_pos_ = -1
    empty_pos, board = _shuffle_()
    _initial_state_ = _state_(board, 0, 0, empty_pos)
    _visited_list_.append(_initial_state_)
    return _visited_list_[0].board  


def reset_game():
    global _initial_state_, _visited_list_, _path_list_, _solved_, _solution_pos_
    _path_list_ = []
    _visited_list_ = []
    _solved_ = False
    _solution_pos_ = -1
    _visited_list_.append(_initial_state_)
    return _visited_list_[0].board


def solve(x):
    global _solution_pos_, _path_list_
    if(x==0):
        _a_star_()
    elif(x==1):
        _breadth_search_()
    elif(x==2):
        _deep_search_()

    while(_solution_pos_ != 0):
        _path_list_.append(_visited_list_[_solution_pos_])
        _solution_pos_ = _visited_list_[_solution_pos_].parent

    return _path_list_
