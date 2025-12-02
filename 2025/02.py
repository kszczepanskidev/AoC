import sys
sys.path.append("..")
from helpers import fetchInput
from re import match

input = fetchInput(__file__)[0].split(',')

def findInvalid(regex):
    result = 0

    for rangeBounds in input:
        start, end = rangeBounds.split('-')
        valueRange = range(int(start), int(end) + 1)
        for value in valueRange:
            if match(regex, str(value)) is not None:
                result += value

    return result

def a(): #64215794229
    return findInvalid(r'^(.+)\1{1}$')

def b(): #85513235135
    return findInvalid(r'^(.+)\1+$')


print(f'a: {a()}')
print(f'b: {b()}')
