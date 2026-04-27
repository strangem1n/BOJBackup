n = int(input())
result = 0

for _ in range(n):
    check = 1
    word = list(input())
    for i in word:
        while word.count(i) >= 2:
            loc = word.index(i)
            word.remove(i)
            if loc != word.index(i):
                check = 0
    result += check

print(result)