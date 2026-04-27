chicken = int(input())
cola, beer = map(int, input().split())

temp = cola // 2 + beer
print(min(chicken, temp))