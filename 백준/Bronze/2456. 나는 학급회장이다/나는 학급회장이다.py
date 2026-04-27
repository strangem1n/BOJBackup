import sys
input = sys.stdin.readline


def chk():
    total = [election[i]['total'] for i in range(3)]
    max_total = max(total)
    max_idx = []

    for idx in range(3):
        if total[idx] == max_total:
            max_idx.append(idx)

    if len(max_idx) == 1:
        return max_idx[0]+1, max_total

    three = [election[i][3] for i in range(3)]
    for i in range(3):
        if i not in max_idx:
            three[i] = 0
    max_three = max(three)
    max_three_idx = []
    for k in max_idx:
        if three[k] == max_three:
            max_three_idx.append(k)

    if len(max_three_idx) == 1:
        return max_three_idx[0]+1, max_total

    two = [election[i][2] for i in range(3)]
    for i in range(3):
        if i not in max_three_idx:
            two[i] = 0
    max_two = max(two)
    max_two_idx = []
    for j in max_three_idx:
        if two[j] == max_two:
            max_two_idx.append(j)

    if len(max_two_idx) == 1:
        return max_two_idx[0]+1, max_total

    return 0, max_total


n = int(input())
election = [{'total': 0, 3: 0, 2: 0} for _ in range(3)]

for _ in range(n):
    score = list(map(int, input().split()))
    for i in range(3):
        election[i]['total'] += score[i]
        if score[i] == 3:
            election[i][3] += 1
        elif score[i] == 2:
            election[i][2] += 1

result = chk()
print(*result)