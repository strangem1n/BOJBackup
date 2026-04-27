import sys
from collections import defaultdict

def get_keys_using_defaultdict(d, val):
    reverse_dict = defaultdict(list)
    for key, value in d.items():
        reverse_dict[value].append(key)
    return reverse_dict[val]

check = {}

n = int(sys.stdin.readline())
for _ in range(n):
    name, log = map(str, sys.stdin.readline().split())
    check[name] = log

current = get_keys_using_defaultdict(check, "enter")
current.sort(reverse=True)

for i in current:
    print(i)