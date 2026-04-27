import sys
input = sys.stdin.readline

def move(spin):
    player[0] += delta[(side + spin) % 4][0]
    camera[0] += delta[(side + spin) % 4][0]
    player[1] += delta[(side + spin) % 4][1]
    camera[1] += delta[(side + spin) % 4][1]
    print(*player, *camera)

def mouse(cw):
    global side
    side = (side + cw) % 4
    camera[0] = player[0] - delta[side][0]
    camera[1] = player[1] - delta[side][1]
    print(*player, *camera)

player = [0, 0]
camera = [0, -1]
side = 0
delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

n = int(input())
for _ in range(n):
    status = input().rstrip()
    if status == 'W':
        move(0)
    elif status == 'D':
        move(1)
    elif status == 'S':
        move(2)
    elif status == 'A':
        move(3)
    elif status == 'MR':
        mouse(1)
    elif status == 'ML':
        mouse(3)
