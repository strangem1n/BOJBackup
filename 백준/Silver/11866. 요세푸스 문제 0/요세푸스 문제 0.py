n, k = map(int, input().split())
num = []
ans = []
for i in range(n):
    num.append(i+1)
checker = k - 1
while len(num) > 0:
    if checker < len(num):
        ans.append(str(num[checker]))
        del num[checker]
        checker += (k - 1)
    else:
        checker = checker - len(num)
print('<'+', '.join(ans)+'>')