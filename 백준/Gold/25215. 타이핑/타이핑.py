import sys
word = list(map(lambda x: True if ord(x) <= 90 else False, sys.stdin.readline().strip()))
dp = [[[False, 0] for _ in range(2)] for _ in range(len(word)+1)]

for i in range(1, len(word)+1):
    dia_temp = []
    star_temp = []
    if dp[i-1][0][0] != word[i-1]:
        dia_temp.append([word[i-1], dp[i-1][0][1]+2])
        star_temp.append([dp[i-1][0][0], dp[i-1][0][1]+2])
    else:
        dia_temp.append([dp[i-1][0][0], dp[i-1][0][1]+1])
        star_temp.append([dp[i-1][0][0], dp[i-1][0][1]+1])
    if dp[i-1][1][0] != word[i-1]:
        dia_temp.append([word[i-1], dp[i-1][1][1]+2])
        star_temp.append([dp[i-1][1][0], dp[i-1][1][1]+2])
    else:
        dia_temp.append([dp[i-1][1][0], dp[i-1][1][1]+1])
        star_temp.append([dp[i-1][1][0], dp[i-1][1][1]+1])
    dia_temp.sort(key=lambda x: x[1])
    star_temp.sort(key=lambda x: x[1])
    dp[i][0] = dia_temp[0]
    dp[i][1] = star_temp[0]
print(min(dp[-1][0][1], dp[-1][1][1]))
