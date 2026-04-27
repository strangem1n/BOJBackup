import sys
ff, fs, sf, ss = map(int, sys.stdin.readline().split())

a = ff
if fs > 0:
    if sf > 0:
        a += min(fs, sf) * 2 + ss
        if fs > sf:
            a += 1
    else:
        a += 1 + ss
if ff == fs == 0:
    b = ss + min(1, sf)
else:
    b = 0
print(max(a, b))
