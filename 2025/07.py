import sys
sys.path.append("..")
from helpers import fetchInput

input = fetchInput(__file__)
input = [list(r) for r in input]
x = input[0].index('S')
y = 1

result = 0

def next_step(target_x, target_y, time_split):
    global result
    if target_y == len(input):
        return

    if input[target_y][target_x] == '.':
        input[target_y][target_x] = '|'
        next_step(target_x, target_y+1, time_split)
    elif input[target_y][target_x] == '|':
        if time_split:
            next_step(target_x, target_y+1, time_split)
        else:
            return
    elif input[target_y][target_x] == '^':
        result += 1
        next_step(target_x-1, target_y, time_split)
        next_step(target_x+1, target_y, time_split)

def a(): #1605
    next_step(x, y, False)

    return result

def b(): #29893386035180
    global result
    result = 1

    next_step(x, y, True)

    return result


print(f'a: {a()}')
print(f'b: {b()}')