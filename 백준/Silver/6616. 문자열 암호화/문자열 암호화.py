import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    word = "".join(input().split()).upper()
    crypt = [""] * len(word)
    cnt = 0
    for i in range(len(word)):
        while i < len(word) and cnt < len(word):
            crypt[i] = word[cnt]
            i += n
            cnt += 1
        if cnt >= len(word):
            break
    print("".join(crypt))
