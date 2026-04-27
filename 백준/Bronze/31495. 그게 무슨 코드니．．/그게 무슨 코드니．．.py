import sys
a = sys.stdin.readline().rstrip()
if a[0] == a[-1] == '"':
    b = a[1:-1]
    if '"' in b or not b:
        print("CE")
    else:
        print(b)
else:
    print("CE")