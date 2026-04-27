import sys
input = sys.stdin.readline
t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    arr.sort()
    longest = arr.pop()
    sum_rest = arr[0] ** 2 + arr[1] ** 2
    print(f"Scenario #{tc}:")
    if longest ** 2 == sum_rest:
        print("yes")
    else:
        print("no")
    print("")