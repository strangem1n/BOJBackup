import sys
input = sys.stdin.readline

n = int(input())
kg = [0] * n
cm = [0] * n
rank = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    kg[i] = x
    cm[i] = y

for i in range(n):
    cnt = 1
    for j in range(n):
        if i != j and kg[j] > kg[i] and cm[j] > cm[i]:
            cnt += 1
    rank[i] = cnt

print(*rank)