import sys
input = sys.stdin.readline

n, m = map(int, input().split())
value = sorted(map(int, input().split()), reverse=True)
cost = sorted(map(int, input().split()))

result = 0
for i in range(min(n, m)):
    benefit = value[i] - cost[i]
    if benefit <= 0:
        break
    else:
        result += benefit
print(result)