import sys
input = sys.stdin.readline

p, n = map(int, input().split())
arr = sorted(map(int, input().split()))
left_time = p
problem_n = n
for i in range(n):
    if left_time > arr[i]:
        left_time -= arr[i]
    else:
        problem_n = i
        break
penalty = 0
penalty_temp = p - (sum(arr[:problem_n]) + 1)
for i in range(problem_n-1, -1, -1):
    penalty += penalty_temp + arr[i]
    penalty_temp += arr[i]
print(problem_n, penalty)
