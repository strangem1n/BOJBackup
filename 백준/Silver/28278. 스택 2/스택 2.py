import sys
input = sys.stdin.readline

stack = [0] * 1000000
top = -1

N = int(input())
for _ in range(N):
    order = input().rstrip()
    if order[0] == "1":
        a, x = map(int, order.split())
        top += 1
        stack[top] = x
    elif order == "2":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif order == "3":
        print(top+1)
    elif order == "4":
        if top == -1:
            print(1)
        else:
            print(0)
    else:
        if top == -1:
            print(-1)
        else:
            print(stack[top])
