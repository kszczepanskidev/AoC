import sys
sys.path.append("..")
from helpers import fetchInput, merge_ranges

input = fetchInput(__file__)

split_index = input.index('')
ranges = [(int(s), int(e)) for s, e in [r.split('-') for r in input[:split_index]]]
products = [int(p) for p in input[split_index+1:]]

def a(): #758
    fresh_products = []

    for product in products:
        if product in fresh_products:
            continue
        for fresh_range in ranges:
            if fresh_range[0] <= product <= fresh_range[1]:
                fresh_products.append(product)
                break

    return len(fresh_products)

def b(): #343143696885053
    return sum([len(r) for r in [range(r[0],r[1]+1) for r in merge_ranges(ranges)]])


print(f'a: {a()}')
print(f'b: {b()}')
