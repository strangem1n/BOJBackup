subjects = int(input())
scores = list(map(int, input().split()))
maxscore = max(scores)
newscores = 0
for i in scores:
    newscores += (i / maxscore * 100)
print(newscores / subjects)