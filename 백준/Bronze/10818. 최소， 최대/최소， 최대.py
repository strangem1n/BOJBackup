_ = input()
n = list(map(int, input().split()))
n.sort()
print(f"{n[0]} {n[-1]}")