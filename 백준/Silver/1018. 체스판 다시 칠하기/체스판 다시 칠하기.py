n, m = map(int, input().split())
chess = []
result = []

for _ in range(n):
    line = list(input())
    chess.append(line)

for i in range(0, n-7):
    for j in range(0, m-7):
        count = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 1:
                    if chess[k][l] == "B":
                        count += 1
                if (k + l) % 2 == 0:
                    if chess[k][l] == "W":
                        count += 1
        result.append(count)
        count = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 1:
                    if chess[k][l] == "W":
                        count += 1
                if (k + l) % 2 == 0:
                    if chess[k][l] == "B":
                        count += 1
        result.append(count)

print(min(result))