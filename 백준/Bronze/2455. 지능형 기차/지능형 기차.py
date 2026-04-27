train = 0
result = 0
for _ in range(4):
    o, i = map(int, input().split())
    train -= o
    train += i
    if train > result:
        result = train
print(result)