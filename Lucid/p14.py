# T-Rex Pushups

n = int(input())

terrain = input().split(" ")
terrain = [int(height) for height in terrain]

count = 0
for i, height in enumerate(terrain):
    if i > 0 and terrain[i-1] - height >= 4:
        count += 1
    
print(count)