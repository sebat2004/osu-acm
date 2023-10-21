# Watering Holes
from collections import defaultdict

logs = int(input())

trackHoles = [set() for _ in range(10001)]
trackDinos = defaultdict(int)

seenHoles = set()
for _ in range(logs):
    dino, hole = input().split(" ")
    dino, hole = dino, int(hole)

    seenHoles.add(hole)
    currHole = trackDinos[dino]
    trackHoles[hole].add(dino)
    if currHole:
        trackHoles[currHole].remove(dino)
    trackDinos[dino] = hole

for hole in seenHoles:
    if hole == 0:
        continue
    output = []
    for d in trackHoles[hole]:
        output.append(d)
    if output:
        print(hole, " ".join(output))
    else:
        print(hole, "n/a")
