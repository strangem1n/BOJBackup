import sys
input = sys.stdin.readline

n, m = map(int, input().split())
u, v = map(int, input().split())
texture = [list(input().rstrip()) for _ in range(u)]
fill_type = input().rstrip()

result = [[None] * 200 for _ in range(200)]

if fill_type == "clamp-to-edge":
    for i in range(u):
        for j in range(v):
            result[i][j] = texture[i][j]
    for i in range(u):
        for j in range(v, 200):
            result[i][j] = result[i][j-1]
    for i in range(u, 200):
        for j in range(v):
            result[i][j] = result[i-1][j]
    for i in range(u, 200):
        for j in range(v, 200):
            result[i][j] = texture[u-1][v-1]

elif fill_type == "repeat":
    for i in range(200):
        for j in range(200):
            result[i][j] = texture[i%u][j%v]

else:
    for i in range(u):
        texture[i] += texture[i][::-1]
    for j in range(u-1, -1, -1):
        texture.append(texture[j])
    for i in range(200):
        for j in range(200):
            result[i][j] = texture[i%(u*2)][j%(v*2)]

for i in range(n):
    for j in range(m):
        print(result[i][j], end="")
    print("")