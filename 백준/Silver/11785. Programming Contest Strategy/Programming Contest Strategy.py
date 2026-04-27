import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n, l = map(int, input().split())
    arr = sorted(map(int, input().split()))
    summary = [0] * n
    summary[0] = arr[0]
    for i in range(1, n):
        summary[i] = summary[i-1] + arr[i]

    last = 0
    score = 0
    cnt = 0
    left_time = l
    for i in range(n):
        if left_time >= arr[i]:
            left_time -= arr[i]
            score += summary[i]
            last = summary[i]
            cnt += 1
        else:
            break
    print(f"Case {tc}: {cnt} {last} {score}")
