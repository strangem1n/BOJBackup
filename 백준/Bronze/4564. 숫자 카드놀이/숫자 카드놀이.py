import sys
input = sys.stdin.readline

def play(n):
    if len(n) == 1:
        return n
    else:
        seperate = map(int, n)
        next_n = 1
        for s in seperate:
            next_n *= s
        return n + ' ' + play(str(next_n))

while True:
    num = input().rstrip()
    if num == '0':
        break
    print(play(num))