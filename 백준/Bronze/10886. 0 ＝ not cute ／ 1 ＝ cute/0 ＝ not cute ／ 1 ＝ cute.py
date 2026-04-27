import sys
input = sys.stdin.readline

arr = [0, 0]
n = int(input())
for _ in range(n):
    arr[int(input())] += 1

if arr[0] > arr[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")