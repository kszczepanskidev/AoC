import sys
sys.path.append("..")
from helpers import fetchInput
from itertools import combinations
from shapely.geometry.polygon import Polygon

input = [[int(v) for v in l.split(',')] for l in fetchInput(__file__)]

def get_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def is_inside(p1, p2):
    global input
    p1x, p2x = min(p1[0], p2[0]), max(p1[0], p2[0])
    p1y, p2y = min(p1[1], p2[1]), max(p1[1], p2[1])
    sqaure = Polygon([(p1x, p1y), (p1x, p2y), (p2x, p2y), (p2x, p1y)])
    polygon = Polygon(input).buffer(1e-13)
    return polygon.contains(sqaure)

squares = sorted([(p1, p2, get_area(p1, p2)) for p1, p2 in combinations(input, 2)], key=lambda x: x[2], reverse=True)

def a(): #4755429952
    return squares[0][2]

def b(): #1429596008
    return next((sq[2] for sq in squares if is_inside(sq[0], sq[1])), None)

print(f'a: {a()}')
print(f'b: {b()}')