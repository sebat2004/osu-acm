# Museum Analytics

from collections import defaultdict

n = int(input())
freq = defaultdict(int)
for _ in range(n):
    dinos = input().split(",")

    for dino in dinos:
        freq[dino] += 1

maxDino = ""
maxVotes = 0
for dino, count in freq.items():
    if count > maxVotes:
        maxDino = dino
        maxVotes = count
print(maxDino)
print(maxVotes)