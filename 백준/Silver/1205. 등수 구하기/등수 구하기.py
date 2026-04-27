import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())
if n > 0:
    rank = list(map(int, input().split()))
    if n == p and new_score <= rank[-1]:
        print(-1)
    else:
        rank.append(new_score)
        rank.sort(reverse=True)
        while len(rank) > p:
            rank.pop()
        for i in range(len(rank)):
            if rank[i] == new_score:
                print(i+1)
                break
else:
    print(1)
