import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word = input().rstrip()
    i = 0
    while i <= len(word)//2:
        if word[i] == word[-(i+1)]:
            i += 1
        else:
            print(f"0 {i+1}")
            break
    else:
        print(f"1 {i}")
