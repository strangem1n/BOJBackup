import sys
input = sys.stdin.readline

n = int(input())
lines = {}
for _ in range(n):
    idx, color = map(int, input().split())
    if lines.get(color):
        lines[color].append(idx)
    else:
        lines[color] = [idx]

result = 0
for line in lines.values():
    if len(line) > 2:
        line.sort()
        result += abs(line[1] - line[0])
        for i in range(1, len(line)-1):
            result += min(abs(line[i] - line[i-1]), abs(line[i+1] - line[i]))
        result += abs(line[-1] - line[-2])
    elif len(line) == 2:
        result += abs(line[1] - line[0]) * 2
print(result)
