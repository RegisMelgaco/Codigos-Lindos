# queen = 2, atack = 1 and empty = 0

import functools as ft


copy_board = lambda board: [row[:] for row in board]
count_queens_in_board = lambda board: ft.reduce(lambda a, p: p.count(2) + a, board, 0)
print_board = lambda board: [*map(print, board)]

def place_queen (position, board):
    b = copy_board(board)
    board_size = len(board[0])

    for i in range(board_size):
        b[position["row"]][i] = 1
        b[i][position["col"]] = 1

        y1 = position["row"] - position["col"] + i
        y2 = position["row"] + position["col"] - i
        if y1 in range(board_size): b[y1][i] = 1
        if y2 in range(board_size): b[y2][i] = 1

    b[position["row"]][position["col"]] = 2
    
    return b

def where_can_place_queen (board):
    positions = []

    for row_indice, row in enumerate(board):
        for col_indice, p in enumerate(row):
            if p == 0: positions.append({"row": row_indice, "col": col_indice})

    return positions

def has_repited_board (boards):
    b = [copy_board(board) for board in boards]
    b.sort()
    
    for i in range(1, len(b)):
        if b[i-1] == b[i]: return True

    return False 

def queens_bfs(n_queens = 8):
    boards_history, next_working_boards, solututions = [], [], []
    working_boards= [[[0 for i in range(n_queens)] for j in range(n_queens)]]

    while len(working_boards) != 0:
        for board_index, board in enumerate(working_boards):
            for pos in where_can_place_queen(board):
                new_board = place_queen(pos, board)
                # if (has_repited_board(boards_history)): print("has repetition on boards_history")
                # if (has_repited_board(working_boards)): print("has repetition on working_board")

                if not (new_board in boards_history):
                    boards_history.append(new_board)
                    next_working_boards.append(new_board)

                    next_board_count = count_queens_in_board(new_board)
                    print(next_board_count, len(working_boards)) # progress
                    if next_board_count == n_queens:
                        solututions.append(new_board)

            working_boards.pop(board_index)
        working_boards = next_working_boards
        boards_history, next_working_boards = [], []

    return solututions

r = queens_bfs(6)

print("the number of answers is:", len(r))
