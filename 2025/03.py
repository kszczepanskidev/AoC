import sys
sys.path.append("..")
from helpers import fetchInput
from re import match

input = fetchInput(__file__)

def a(): #16812
    result = 0
    for string in input:
        maxTens = max([int(char) for char in string[:-1]])
        tensIndex = string.index(str(maxTens)) + 1
        maxOnes = max([int(char) for char in string[tensIndex:]])
        result += maxTens * 10 + maxOnes

    return result

def b(): #166345822896410
    result = 0
    for string in input:    
        selected = ''
        toDrop = len(string) - 12
        for index, char in enumerate(string):
            if len(selected) == 12:
                break

            if toDrop == 0:
                selected += char
                continue

            checkSlice = string[index+1:index+toDrop+1]
            maxCheck = max([int(char) for char in checkSlice])
            if int(char) >= maxCheck:
                selected += char
                continue
            
            toDrop -= 1
                
        result += int(selected)

    return result


print(f'a: {a()}')
print(f'b: {b()}')