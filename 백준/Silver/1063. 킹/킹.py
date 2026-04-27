import sys
input = sys.stdin.readline

k, s, n = input().split()
kj, ki = ord(k[0]) - 65, -(int(k[1]) - 8)
sj, si = ord(s[0]) - 65, -(int(s[1]) - 8)


for _ in range(int(n)):
    move = input().rstrip()
    di = dj = 0
    for m in move:
        if m == 'R':
            dj += 1
        elif m == 'L':
            dj -= 1
        elif m == 'B':
            di += 1
        elif m == 'T':
            di -= 1

    kni, knj = ki + di, kj + dj
    if 0 <= kni < 8 and 0 <= knj < 8:
        if kni == si and knj == sj:
            sni, snj = si + di, sj + dj
            if 0 <= sni < 8 and 0 <= snj < 8:
                ki, kj, si, sj = kni, knj, sni, snj
        else:
            ki, kj = kni, knj

print(chr(kj + 65), end='')
print(-ki + 8)
print(chr(sj + 65), end='')
print(-si + 8)
