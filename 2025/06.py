import sys
sys.path.append("..")
from helpers import fetchInput, transpose

input = [r+' ' for r in fetchInput(__file__, False)]
operations = [v for v in input[-1].split() if v != ' ']


def a(): #4805473544166
    global input
    new_input = [[n+' ' for n in v if n != ''] for v in [l.split(' ') for l in input[:-1]]]
    new_input = [row.split(' ')[:-1] for row in transpose(new_input)]
    result = 0

    for col, operation in zip(new_input, operations):
        result += eval(operation.join(col))

    return result

def b(): #8907730960817
    result = 0

    values = []

    for index, _ in enumerate(input[0]):
        column = [input[r][index] for r in range(len(input) - 1)]
        if all([c == ' ' for c in column]):
            result += eval(operations.pop(0).join(values))
            values = []
            continue
        else:
            values.append(''.join(column).strip())

    return result


print(f'a: {a()}')
print(f'b: {b()}')
