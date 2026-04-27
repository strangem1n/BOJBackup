S = input()
chk = 'SciComLove'

result = 0
for i in range(10):
    if S[i] != chk[i]:
        result += 1
print(result)