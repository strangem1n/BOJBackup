import sys
input = sys.stdin.readline

_ = input()
problem = 0
while True:
    command = input().rstrip()
    if command == "문제":
        problem += 1
    elif command == "고무오리":
        if problem > 0:
            problem -= 1
        else:
            problem += 2
    else:
        break
if problem == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")