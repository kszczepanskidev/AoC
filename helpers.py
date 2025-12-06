from os import environ
from re import match
from requests import get
from itertools import combinations


def fetchInput(name, strip=True):
    headers = {'Cookie': f'session={environ["AOCCOOKIE"]}'}
    name = name.split('/')
    day = match(r'0?(\d*)[ab]?.py', name[-1]).group(1)
    year = name[-2]

    input = get(f'https://adventofcode.com/{year}/day/{day}/input', headers=headers).text.splitlines()
    return [l.strip() if strip else l for l in input]

def loadFile(name):
    return [l.strip() for l in open(f'{name.replace("b.py","").replace(".py","")}-in.txt').readlines()]

def chunks(array, size):
    for i in range(0, len(array), size):
        yield array[i:i+size]

def flatten(list):
    return [item for sublist in list for item in sublist]

def transpose(grid):
    return [''.join(list(i)) for i in zip(*grid)]

def replace(string, character, index):
    if index not in range(len(string)):
        return string
    return string[:index] + character + string[index+1:]

def merge_ranges(ranges):
    def find_overlap(list):
        for range1, range2 in combinations(list, 2):
            min1, max1 = range1
            min2, max2 = range2

            if min1 > max2 or max1 < min2:
                continue
            else:
                return range1, range2

        return None

    merged_list = ranges
    while True:
        overlap = find_overlap(merged_list)
        if not overlap:
            return merged_list
        range1, range2 = overlap

        merged_list.remove(range1)
        merged_list.remove(range2)
        range_values = range1 + range2
        merged_list.append((min(range_values), max(range_values)))
