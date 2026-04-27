import sys
input = sys.stdin.readline

ih, im = map(int, input().split())
arr = [ih // 10, ih % 10, im // 10, im % 10]

th, tm = map(int, input().split())
t1, t2, t3, t4 = th // 10, th % 10, tm // 10, tm % 10

n = int(input())
cnt = 0

end = False
while True:
    if arr == [t1, t2, t3, t4]:
        end = True
    if n in arr:
        cnt += 1
    arr[3] += 1
    if arr[3] > 9:
        arr[2] += 1
        arr[3] = 0
    if arr[2] > 5:
        arr[1] += 1
        arr[2] = 0
    if arr[1] > 9:
        arr[0] += 1
        arr[1] = 0
    if end:
        break

print(cnt)
