n = int(input())
for _ in range(n):
    l = input().split(" ")
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])

    half = (a + b)/2
    dist = abs(half - a)
    divisions = dist // c
    remainder = dist % c
    if remainder:
        print(int(divisions + 1))
    else:
        print(int(divisions))
