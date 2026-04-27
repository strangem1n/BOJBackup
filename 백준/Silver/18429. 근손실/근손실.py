from itertools import permutations

def muscle(kit_list, day, loss):
    body = 0
    for i in range(day):
        body += (kit_list[i] - loss)
        if body < 0:
            return 0
    return 1


n, k = map(int, input().split())
kit = list(map(int, input().split()))

all_list = permutations(kit, n)
result = 0
for a in all_list:
    result += muscle(a, n, k)
print(result)
