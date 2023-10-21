# Most Recent Common Ancestor

from collections import defaultdict

n = int(input())

edges = defaultdict(list)

for _ in range(n):
    ancestor, descendant = input().split(" -- ")

    edges[descendant].append(ancestor)

first = input()
second = input()

def getPath(anc, path):
    path.append(anc)
    if not edges[anc]:
        return path
    
    for a in edges[anc]:
        return getPath(a, path)

firstPath = getPath(second, [])

secondPath = getPath(first, [])

for a in firstPath:
    if a in secondPath:
        print(a)
        break


