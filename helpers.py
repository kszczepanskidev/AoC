from os import environ
from re import match
from requests import get


def fetchInput(name):
    headers = {'Cookie': f'session={environ["AOCCOOKIE"]}'}
    name = name.split('/')
    day = match(r'0?(\d*)[ab]?.py', name[-1]).group(1)
    year = name[-2]

    input = get(f'https://adventofcode.com/{year}/day/{day}/input', headers=headers).text.splitlines()
    return [l.strip() for l in input]

def loadFile(name):
    return [l.strip() for l in open(f'{name.replace("b.py","").replace(".py","")}-in.txt').readlines()]

def chunks(array, size):
    for i in range(0, len(array), size):
        yield array[i:i+size]

def flatten(list):
    return [item for sublist in list for item in sublist]

def transpose(grid):
    return [''.join(list(i)) for i in zip(*grid)]
