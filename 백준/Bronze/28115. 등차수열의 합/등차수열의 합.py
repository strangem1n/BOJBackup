import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print('YES')
    print(1)
    print(arr[0]-1)
elif n == 2:
    d = arr[1]-arr[0]
    print('YES')
    print(1, 1+(2*d))
    print(arr[0]-1, arr[0]-1-d)
else:
    d = arr[1] - arr[0]
    for i in range(n-1):
        if arr[i]+d != arr[i+1]:
            print('NO')
            break
    else:
        print('YES')
        for k in range(n):
            print(1+(2*k*d), end=' ')
        print('')
        for k in range(n):
            print(arr[0]-1-(k*d), end=' ')
        print('')
