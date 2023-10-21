from collections import defaultdict
from functools import cache

n, m, f = input().split(" ")
n, m, f = int(n), int(m), int(f)

foods = input().split(" ")
foods = [int(loc) for loc in foods]

edges = defaultdict(list)

for _ in range(m):
    src, dest = input().split(" ")
    src, dest = int(src), int(dest)
    edges[src].append(dest)

for key, value in edges.items():
    value.sort(reverse=True)

minEatens = [0 for _ in range(n)]

def dfs(node, eaten, length, minEatens):
    eaten += foods[node - 1]
    if node == n and eaten >= f:
        return length
    elif node == n:
        return 0
    
    minPath = 150001
    for dest in edges[node]:
        if eaten > minEatens[dest-1]:
            l = dfs(dest, eaten, length + 1, minEatens)
            if l:
                minPath = min(minPath, l)
            else:
                minEatens[dest-1] = max(minEatens[dest-1], eaten)
                print("True")
        else:
            print("hit")

    return minPath
    

print(dfs(1, 0, 0, minEatens))

