import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    wow = input().rstrip()
    result = 0
    for i in range(len(wow)-2):
        if wow[i:i+3] == "WOW":
            result += 1
    print(result)