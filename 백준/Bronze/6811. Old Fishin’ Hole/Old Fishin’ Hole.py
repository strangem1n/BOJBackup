brown = int(input())
northern = int(input())
yellow = int(input())
limit = int(input())

cnt = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if 0 < k*brown + j*northern + i*yellow < limit+1:
                cnt += 1
                print(f'{k} Brown Trout, {j} Northern Pike, {i} Yellow Pickerel')
print(f'Number of ways to catch fish: {cnt}')
