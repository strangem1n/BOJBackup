import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cats = sorted(map(int, input().split()))

left = 0
right = n-1
happy = 0
while left < right:
    if cats[left] + cats[right] <= k:
        happy += 1
        left += 1
        right -= 1
    else:
        right -= 1
print(happy)