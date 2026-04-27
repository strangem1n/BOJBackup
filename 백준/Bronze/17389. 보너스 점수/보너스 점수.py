n = int(input())
ox = input()
bonus = 0
result = 0
for i in range(n):
    if ox[i] == 'O':
        result += i+1+bonus
        bonus += 1
    else:
        bonus = 0
print(result)
