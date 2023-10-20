tests = int(input())
for _ in range(tests):
    n, c, d = input().split(" ")
    arr = input().split(" ")
    arr = [int(i) for i in arr]
    arr.sort()
    cost = 0
    for i, num in enumerate(arr):
        if arr[i-1] == num and i > 0:
            cost += int(c)
        elif arr[i-1] != num - 1 and i > 0:
            diff = (num - arr[i-1] - 1) * int(d)
            remainingEls = (int(n) - i) * int(c)
            cost += min(diff, remainingEls)
    print(cost)


