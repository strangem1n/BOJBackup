n = int(input())

stack = []

for i in range(n // 5 + 1):
    for j in range(n // 3 + 1):
        if n == (5 * i + 3 * j):
            stack.append(i+j)

if len(stack) >= 1:
    print(min(stack))
else:
    print(-1)