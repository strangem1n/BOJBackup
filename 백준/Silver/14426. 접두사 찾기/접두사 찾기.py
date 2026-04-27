import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
            if node.is_end:
                return True
        node.is_end = True
        return False

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

n, m = map(int, input().split())
t = Trie()
for _ in range(n):
    w = input().rstrip()
    t.insert(w)
cnt = 0
for _ in range(m):
    chk = input().rstrip()
    if t.search(chk):
        cnt += 1
print(cnt)