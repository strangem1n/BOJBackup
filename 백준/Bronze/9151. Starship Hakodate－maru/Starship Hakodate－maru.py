import sys
from bisect import bisect_left

arr1 = [i ** 3 for i in range(54)]
arr2 = [(i * (i+1) * (i+2)) // 6 for i in range(96)]

fuel = {}
for a in arr1:
    for b in arr2:
        fuel[a+b] = True
arr = sorted(fuel.keys())

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    idx = bisect_left(arr, n)
    if n == arr[idx]:
        print(n)
    else:
        print(arr[idx-1])