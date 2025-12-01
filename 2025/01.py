import sys
sys.path.append("..")
from helpers import fetchInput
input = fetchInput(__file__)

def a():
    knob = 50
    result = 0

    for action in input:
        result += 1 if knob == 0 else 0

        diff = int(action[1:])
        rot = action[0]
        match rot:
            case 'R':
                knob += diff
                while knob > 99:
                    knob -= 100
            case 'L':
                knob -= diff
                while knob < 0:
                    knob += 100

    return result

def b():
    knob = 50
    result = 0

    for action in input:
        diff = int(action[1:])
        rot = action[0]
        match rot:
            case 'R':
                knob += diff
                while knob > 99:
                    result += 1
                    knob -= 100
            case 'L':
                start = knob
                knob -= diff
                while knob < 0:
                    if start != 0:
                        result += 1
                    knob += 100
                    start = knob
                if knob == 0:
                    result += 1

    return result


print(f'a: {a()}')
print(f'b: {b()}')
