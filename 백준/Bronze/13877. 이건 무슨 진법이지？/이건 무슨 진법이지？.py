import sys
input = sys.stdin.readline

def solve(num, rule):
    result = 0
    for i in range(len(num)):
        result += int(num[-(i+1)]) * (rule ** i)
    return(result)

n = int(input())
for t in range(1, n+1):
    _, num = input().split()
    if '8' in num or '9' in num:
        octa = 0
    else:
        octa = solve(num, 8)
    hexa = solve(num, 16)
    print(t, octa, int(num), hexa)

    
   