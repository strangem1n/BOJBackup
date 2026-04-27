k = int(input())
b = 0
a = 1
for _ in range(k-1):
    b, a = a, b+a
print(f'{b} {a}')