import sys
input = sys.stdin.readline

n, l = map(int, input().split())
max_line = max_num = 0
for _ in range(n):
    zebra = input().rstrip()
    idx = line = 0
    while idx < l:
        if zebra[idx] == '1':
            line += 1
            while idx < l and zebra[idx] == '1':
                idx += 1
        else:
            idx += 1
    if max_line < line:
        max_line = line
        max_num = 1
    elif max_line == line:
        max_num += 1
print(max_line, max_num)