import sys
input = sys.stdin.readline

n = int(input())
prev_word = input().rstrip()
cnt = 1
used = {prev_word: True}
for _ in range(n-1):
    word = input().rstrip()
    if prev_word[-1] != word[0]:
        print(f"Player {cnt+1} lost")
        break

    if used.get(word):
        print(f"Player {cnt+1} lost")
        break

    used[word] = True
    prev_word = word
    cnt = (cnt + 1) % 2
else:
    print('Fair Game')