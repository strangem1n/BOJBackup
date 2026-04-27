import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input())
    winner = max_num = -1
    for i in range(n):
        if max_num < arr[i]:
            winner = i
            max_num = arr[i]
        elif max_num == arr[i]:
            winner = -1
    if winner == -1:
        print('no winner')
    else:
        if max_num > sum(arr) // 2:
            print(f'majority winner {winner+1}')
        else:
            print(f'minority winner {winner+1}')
