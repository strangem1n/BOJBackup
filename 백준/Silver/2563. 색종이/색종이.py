n = int(input())
paper = []
for i in range(100):
    for j in range(100):
        unit = [i, j]
        paper.append(unit)

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            try:
                color = [x+i, y+j]
                paper.remove(color)
            except ValueError:
                pass
    
print(10000 - len(paper))