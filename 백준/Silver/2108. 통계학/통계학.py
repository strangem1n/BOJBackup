import sys
input = sys.stdin.readline


def realround(n):
    if n > 0:
        if n - int(n) == 0.5:
            return int(n)+1
        else:
            return round(n)
    elif n == 0:
        return 0
    else:
        n = -1 * n
        return -1 * realround(n)


N = int(input())
arr = [int(input()) for _ in range(N)]

print(realround(sum(arr)/N))

cnt_arr = [0]*8001
new_arr = [0]*N

for i in range(N):
    cnt_arr[arr[i]+4000] += 1

m = max(cnt_arr)
mode = cnt_arr.index(m)
for i in range(mode + 1, 8001):
    if cnt_arr[i] == m:
        mode = i
        break
mode -= 4000


for i in range(8000):
    cnt_arr[i+1] += cnt_arr[i]
for i in range(N):
    cnt_arr[arr[i]+4000] -= 1
    new_arr[cnt_arr[arr[i]+4000]] = arr[i]

print(new_arr[N//2])
print(mode)
print(new_arr[-1] - new_arr[0])
