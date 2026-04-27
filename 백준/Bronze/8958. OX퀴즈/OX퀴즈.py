n = int(input())
for _ in range(n):
    result = 0
    answer = list(input().split('X'))
    while '' in answer:
        answer.remove('')
    for i in answer:
        correct = i.count('O')
        for j in range(correct):
            result += j + 1
    print(result)
