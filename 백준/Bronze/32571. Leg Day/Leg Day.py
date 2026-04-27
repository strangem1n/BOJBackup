n = int(input())
cycle = [None] * n
for i in range(n):
    word = input()
    for j in range(2, len(word)):
        if len(word) > 3 and word[j-4:j] == 'rest':
            cycle[i] = '😴'
            break
        elif word[j-3:j] == 'leg':
            cycle[i] = '🦵'
    else:
        if cycle[i]:
            continue
        else:
            cycle[i] = '💪'

day = 0
for week in range(1, 6):
    print(week, end=' ')
    for _ in range(7):
        print(cycle[day%n], end='')
        day += 1
        if day == 31:
            break
    print('')
