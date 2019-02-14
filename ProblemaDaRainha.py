# a program that find all possible possicions for 8 queens in a 8 by 8 chess board where they can't atack witch other
# 2 == has a queen in this possition, 1 == a queen can atack here and 0 == can place queen

import functools as ft



copy_list = lambda list: list[:]

def has_repetition (list):
    sorted_list = copy_list(list)
    sorted_list.sort()
    for i in range(1, 8):
        if sorted_list[i-1] == sorted_list[i]:
            return True
    return False

calc_diagonal1 = lambda queen_position: queen_position['row'] + queen_position['col']
calc_diagonal2 = lambda queen_position: queen_position['row'] - queen_position['col']

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

def can_atack (board):
    diagonals1, diagonals2 = [], []
    for i, p in enumerate(board):
        diagonals1.append(calc_diagonal1({"row": i, "col": p}))
        diagonals2.append(calc_diagonal2({"row": i, "col": p}))

    if has_repetition(diagonals1) or has_repetition(diagonals2):
        return True
    else:
        return False

def QueensProblem ():
    # each queen has on col and only change line
    solutions = []
    permutations = []

    for p_solution in permute([0,1,2,3,4,5,6,7]):
        if (not can_atack(p_solution)):
            solutions.append(copy_list(p_solution))

    return solutions

solutions = QueensProblem()
print("numero de soluções encontradas:", len(solutions))
print("as soluções são:\n")
for s in solutions:
    print(s)