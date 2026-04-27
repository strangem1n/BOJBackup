import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    ancestor, length = map(int, input().split())
    chk = [1] * length
    me = input().rstrip()
    for _ in range(ancestor):
        anc = input().rstrip()
        for i in range(length):
            if chk[i] == 1 and me[i] == anc[i]:
                chk[i] = 0
    print(f"Data Set {tc}:")
    print(f"{sum(chk)}/{length}")
    print("")
