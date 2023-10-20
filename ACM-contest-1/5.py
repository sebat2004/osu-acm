t = int(input())
for _ in range(t):
    got = False
    n = int(input())
    l = input().split(" ")
    for i in range(n):
        if int(l[i]) <= i + 1:
            got = True
            print("YES")
            break
    if not got:
        print("NO")