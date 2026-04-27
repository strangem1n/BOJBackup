observe = int(input())
cow_info = {}
result = 0
for _ in range(observe):
    cow, status = map(int, input().split())
    if cow_info.get(cow) == None:
        cow_info[cow] = status
    else:
        if cow_info[cow] == status:
            pass
        else:
            result += 1
            cow_info[cow] = status
print(result)