import sys
input = sys.stdin.readline

n = int(input())
stack = [[0, 0, -1]]
result = [0] * n
try:
    for i in range(n):
        level = int(input())
        if stack[-1][0] + 1 == level:
            stack.append([level, 1, i-1])
        elif stack[-1][0] == level:
            stack[-1][1] += 1
        else:
            while stack[-1][0] != level:
                lv, num, idx = stack.pop()
                result[idx] = num
            stack[-1][1] += 1
    while stack:
        lv, num, idx = stack.pop()
        result[idx] = num
    for r in result:
        print(r)
except:
    print(-1)
