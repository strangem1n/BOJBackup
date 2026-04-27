import sys

arr = ['a', 'e', 'i', 'o', 'u']
while True:
    word = sys.stdin.readline().rstrip()
    if word == '#':
        break
    ans = 0
    word = word.lower()
    for i in word:
        if i in arr:
            ans += 1
    print(ans)