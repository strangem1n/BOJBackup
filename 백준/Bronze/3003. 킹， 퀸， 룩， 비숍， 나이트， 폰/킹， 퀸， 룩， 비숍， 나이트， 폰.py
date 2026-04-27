lost = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
correct = []
for i in range(len(chess)):
    correct.append(chess[i]-lost[i])
print(*correct)