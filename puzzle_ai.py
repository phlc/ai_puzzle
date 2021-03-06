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


# Check if is Solvable
def _is_solvable_(board):
    total = 0
    for i in range(9):
        number = board[i//3][i%3]
        if(number != 9):
            for j in range(i+1, 9):
                if(number > board[j//3][j%3]):
                    total += 1
    return total%2 == 0



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


# state = board, parent state, position on _visiteds_, empty position on board, level on tree, heuristic value
class _state_:
    def __init__(self, board, parent, index, empty_pos, tree_level = 0, heuristic=0):
        self.board = board
        self.parent = parent
        self.index = index
        self.empty_pos = empty_pos
        self.tree_level = tree_level
        self.heuristic = heuristic
        


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

# Calculate Heuristic (level options - if considered A star - if not greedy search)
def heuristic_manhattan(board, level=0):
    all_distances = level
    for i in range(3):
        for j in range(3):
            if(board[i][j] == 1):
                all_distances += (abs(i-0)+abs(j-0))
            elif(board[i][j] == 2):
                all_distances += (abs(i-0)+abs(j-1))
            elif(board[i][j] == 3):
                all_distances += (abs(i-0)+abs(j-2))
            elif(board[i][j] == 4):
                all_distances += (abs(i-1)+abs(j-0))
            elif(board[i][j] == 5):
                all_distances += (abs(i-1)+abs(j-1))
            elif(board[i][j] == 6):
                all_distances += (abs(i-1)+abs(j-2))
            elif(board[i][j] == 7):
                all_distances += (abs(i-2)+abs(j-0))
            elif(board[i][j] == 8):
                all_distances += (abs(i-2)+abs(j-1))
    return all_distances

def insert_priority(list, state):
    insert_pos = 0
    while(insert_pos < len(list) and list[insert_pos].heuristic < state.heuristic):
        insert_pos += 1
    list.insert(insert_pos, state)

# A Star search
def _a_star_():
    global _visited_list_, _solution_pos_, _solved_, _initial_state_
    
    priority_queue = []
    priority_queue.append(_initial_state_)

    while(not _solved_ and len(priority_queue)>0):
        state = priority_queue.pop(0)
        board = state.board
        index = state.index
        parent_level = state.tree_level
        empty_lin, empty_col = state.empty_pos

        print(state.board, state.heuristic)
        print(len(_visited_list_))

        if(not _solved_ and 0 <= empty_lin-1):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin-1][empty_col]
            new_board[empty_lin-1][empty_col] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin-1, empty_col), 
                                    parent_level+1, heuristic_manhattan(new_board, parent_level+1))
                _visited_list_.append(new_state)
                insert_priority(priority_queue, new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True
        
        if(not _solved_ and 0<= empty_col-1):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin][empty_col-1]
            new_board[empty_lin][empty_col-1] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin, empty_col-1), 
                                    parent_level+1, heuristic_manhattan(new_board, parent_level+1))
                _visited_list_.append(new_state)
                insert_priority(priority_queue, new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True
        
        if(not _solved_ and empty_col+1 < 3):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin][empty_col+1]
            new_board[empty_lin][empty_col+1] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin, empty_col+1), 
                                    parent_level+1, heuristic_manhattan(new_board, parent_level+1))
                _visited_list_.append(new_state)
                insert_priority(priority_queue, new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True

        if(not _solved_ and empty_lin+1 < 3):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin+1][empty_col]
            new_board[empty_lin+1][empty_col] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin+1, empty_col), 
                                    parent_level+1, heuristic_manhattan(new_board, parent_level+1))
                _visited_list_.append(new_state)
                insert_priority(priority_queue, new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True    
    

# Breadth First Search
def _breadth_search_():
    global _visited_list_, _solution_pos_, _solved_, _initial_state_
    
    queue = []
    queue.append(_initial_state_)

    while(not _solved_ and len(queue)>0):
        state = queue.pop(0)
        board = state.board
        index = state.index
        empty_lin, empty_col = state.empty_pos

        print(state.board, state.heuristic)
        print(len(_visited_list_))

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
        

# Greedy Search
def _greedy_search_():
    global _visited_list_, _solution_pos_, _solved_, _initial_state_
    
    priority_queue = []
    priority_queue.append(_initial_state_)

    while(not _solved_ and len(priority_queue)>0):
        state = priority_queue.pop(0)
        board = state.board
        index = state.index
        parent_level = state.tree_level
        empty_lin, empty_col = state.empty_pos

        print(state.board, state.heuristic)
        print(len(_visited_list_))

        if(not _solved_ and 0 <= empty_lin-1):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin-1][empty_col]
            new_board[empty_lin-1][empty_col] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin-1, empty_col), 
                                    parent_level+1, heuristic_manhattan(new_board))
                _visited_list_.append(new_state)
                insert_priority(priority_queue, new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True
        
        if(not _solved_ and 0<= empty_col-1):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin][empty_col-1]
            new_board[empty_lin][empty_col-1] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin, empty_col-1), 
                                    parent_level+1, heuristic_manhattan(new_board))
                _visited_list_.append(new_state)
                insert_priority(priority_queue, new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True
        
        if(not _solved_ and empty_col+1 < 3):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin][empty_col+1]
            new_board[empty_lin][empty_col+1] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin, empty_col+1), 
                                    parent_level+1, heuristic_manhattan(new_board))
                _visited_list_.append(new_state)
                insert_priority(priority_queue, new_state)
                if(is_solution(new_board)):
                    _solution_pos_ = new_index
                    _solved_ = True

        if(not _solved_ and empty_lin+1 < 3):
            new_board = copy_board(board)
            new_board[empty_lin][empty_col] = new_board[empty_lin+1][empty_col]
            new_board[empty_lin+1][empty_col] = 9
            if(not in_visited(new_board)):
                new_index = len(_visited_list_)
                new_state = _state_(new_board, index, new_index, (empty_lin+1, empty_col), 
                                    parent_level+1, heuristic_manhattan(new_board))
                _visited_list_.append(new_state)
                insert_priority(priority_queue, new_state)
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
    solvable = _is_solvable_(board)
    return (solvable, _visited_list_[0].board)


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
        _greedy_search_()

    print(_visited_list_[_solution_pos_].board, _visited_list_[_solution_pos_].heuristic)
    print(len(_visited_list_))

    while(_solution_pos_ != 0):
        _path_list_.append(_visited_list_[_solution_pos_])
        _solution_pos_ = _visited_list_[_solution_pos_].parent


    return (_path_list_, len(_visited_list_))
