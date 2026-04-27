import sys

n, m = map(int, sys.stdin.readline().split())
pocket_name_num = {}
for i in range(n):
    name = sys.stdin.readline().rstrip()
    pocket_name_num[name] = i + 1

pocket_num_name = {v:k for k, v in pocket_name_num.items()}

for _ in range(m):
    search = sys.stdin.readline().rstrip()
    try:
        search = int(search)
        print(pocket_num_name.get(search))
    except ValueError:
        print(pocket_name_num.get(search))