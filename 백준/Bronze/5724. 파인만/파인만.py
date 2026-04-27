import sys
input = sys.stdin.readline
arr = [i**2 for i in range(1, 101)]
for i in range(1, 100):
    arr[i] += arr[i-1]
while True:
    n = int(input())
    if n == 0:
        break
    print(arr[n-1])
