participate = int(input())
tshirt = list(map(int, input().split()))
t, p = map(int, input().split())
tcount = 0
for i in tshirt:
    tcount += i // t
    if i % t > 0:
        tcount += 1
print(tcount)
pcount = participate // p
print(pcount, participate % p)