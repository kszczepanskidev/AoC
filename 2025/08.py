import sys
sys.path.append("..")
from helpers import fetchInput
from math import dist, prod
from itertools import combinations

input = [[int(v) for v in l.split(',')] for l in fetchInput(__file__)]

pairs = sorted([(p1, p2, dist(p1, p2)) for p1, p2 in combinations(input, 2)], key=lambda x: x[2])
connection_limit = 1000

def solve_connections(variant):
    global pairs, connection_limit

    circuits = []
    connections = 0

    for p1, p2, _ in pairs:
        if variant == 'a' and connections == connection_limit:
            break

        connection1 = next((circuit for circuit in circuits if p1 in circuit), None)
        connection2 = next((circuit for circuit in circuits if p2 in circuit), None)
        connections += 1
        if not connection1 and not connection2:
            circuits.append([p1, p2])
        elif connection1 == connection2:
            continue
        elif connection1 and not connection2:
            connection1.append(p2)
        elif not connection1 and connection2:
            connection2.append(p1)
        elif connection1 and connection2:
            connection1 += connection2
            circuits.remove(connection2)

        if variant == 'b' and len(circuits) == 1 and len(circuits[0]) == len(input):
            return p1[0] * p2[0]

    if variant == 'a':
        return prod([len(c) for c in sorted(circuits, key=lambda c: len(c), reverse=True)[:3]])

def a(): #63920
    return solve_connections('a')

def b(): #1026594680
    return solve_connections('b')


print(f'a: {a()}')
print(f'b: {b()}')