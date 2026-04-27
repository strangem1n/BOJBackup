import sys
input = sys.stdin.readline

a, b = map(int, input().split())
record_a = [0] * 10
record_b = [0] * 10

for i in range(9, -1, -1):
    if a >= 2 ** i:
        a -= 2 ** i
        record_a[i] = 1
    if b >= 2 ** i:
        b -= 2 ** i
        record_b[i] = 1

result = 0
for i in range(10):
    if record_a[i] + record_b[i] == 1:
        result += 2 ** i
print(result)
    