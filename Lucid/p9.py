# Longest Food Chain

"""
Many dinosaurs survive by eating other dinosaurs.
In this problem we want to determine the longest chain of dinosaurs from 
herbivore to apex predator.
"""

from collections import defaultdict
from functools import cache

n = int(input())

adj = defaultdict(list)

seenAnimals = set()

for _ in range(n):
    if n == 0:
        break
    predPreys = input()

    pred = predPreys[0:1]
    seenAnimals.add(pred)

    preys = predPreys[5:].split(", ")

    for prey in preys:
        seenAnimals.add(prey)
        adj[prey].append(pred)

@cache
def dfs(node, length):
    if not adj[node]:
        return length
    
    maxLength = 0
    for pred in adj[node]:
        result = dfs(pred, length + 1)
        maxLength = max(result, maxLength)

    return maxLength

res = 0
for node in seenAnimals:
    res = max(res, dfs(node, 1))

print(res)
