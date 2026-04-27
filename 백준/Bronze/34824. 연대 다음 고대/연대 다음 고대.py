import sys
input = sys.stdin.readline

n = int(input())
while True:
    c = input().rstrip()
    if c == "yonsei":
        print("Yonsei Won!")
    elif c == "korea":
        print("Yonsei Lost...")
    else:
        continue
    break
