import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    tri = sorted(map(int, input().split()))
    if tri[2] >= tri[0] + tri[1]:
        print(f"Case #{tc}: invalid!")
    else:
        if tri[0] == tri[1] == tri[2]:
            print(f"Case #{tc}: equilateral")
        elif tri[0] == tri[1] or tri[1] == tri[2] or tri[0] == tri[2]:
            print(f"Case #{tc}: isosceles")
        else:
            print(f"Case #{tc}: scalene")
