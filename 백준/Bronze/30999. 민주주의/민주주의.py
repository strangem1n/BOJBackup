import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 0
for _ in range(n):
    status = input().rstrip()
    chk = 0
    for ox in status:
        if ox == "O":
            chk += 1
    if chk > (m // 2):
        result += 1
print(result)