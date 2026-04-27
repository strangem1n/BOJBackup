import sys
input = sys.stdin.readline

def realround(n):
    if n - int(n) == 0.5:
        return int(n)+1
    else:
        return round(n)


N = int(input())
if N == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(N)]
    cnt_arr = [0]*31
    new_arr = [0]*N
    cut = realround(N * 0.15)

    for i in range(N):
        cnt_arr[arr[i]] += 1
    for i in range(30):
        cnt_arr[i+1] += cnt_arr[i]
    for i in range(N):
        cnt_arr[arr[i]] -= 1
        new_arr[cnt_arr[arr[i]]] = arr[i]

    result = 0
    for i in range(cut, N-cut):
        result += new_arr[i]
    print(realround(result / (N - 2*cut)))
