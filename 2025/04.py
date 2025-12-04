import sys
sys.path.append("..")
from helpers import fetchInput, replace
from re import match

input = fetchInput(__file__)
_width = len(input[0]) - 1
_height = len(input) - 1

def find_neighbours_count(r,c):
    neighbours = []
    # above
    if r>0:
        if c>0:
            neighbours.append(input[r-1][c-1])
        if c<_width:
            neighbours.append(input[r-1][c+1])
        neighbours.append(input[r-1][c])
    # below
    if r<_height:
        if c>0:
            neighbours.append(input[r+1][c-1])
        if c<_width:
            neighbours.append(input[r+1][c+1])
        neighbours.append(input[r+1][c])
    # sides
    if c>0:
        neighbours.append(input[r][c-1])
    if c<_width:
        neighbours.append(input[r][c+1])

    return len([roll for roll in neighbours if roll == "@"])

def a(): #1445
    result = 0

    for r, row in enumerate(input):
        for c, char in enumerate(row):
            if char == '.':
                continue
            if find_neighbours_count(r,c) < 4:
                result += 1

    return result

def b(): #8317
    result = 0
    
    while True:
        clear_indexes = []
        for r, row in enumerate(input):
            for c, char in enumerate(row):
                if char == '.':
                    continue
                if find_neighbours_count(r,c) < 4:
                    clear_indexes.append((r,c))
                    result += 1

        if clear_indexes == []:
            break

        for r,c in clear_indexes:
            input[r] = replace(input[r], '.', c)

    return result


print(f'a: {a()}')
print(f'b: {b()}')