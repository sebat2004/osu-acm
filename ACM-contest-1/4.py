t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for _ in range(n):
        l = input().split(" ")
        a = int(l[0])
        b = int(l[1])
        if a > b:
            count += 1
    print(count)