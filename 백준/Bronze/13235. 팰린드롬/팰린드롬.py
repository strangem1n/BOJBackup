import sys
from collections import deque
input = sys.stdin.readline

def solve(word):
    while len(word) > 1:
        if word[0] != word[-1]:
            return 'false'
        word.popleft()
        word.pop()
    return 'true'

w = deque(list(input().rstrip()))
print(solve(w))
