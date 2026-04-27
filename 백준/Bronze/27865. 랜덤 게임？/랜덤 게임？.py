import sys

n = int(sys.stdin.readline())
while True:
    print("? 1")
    sys.stdout.flush()
    ans = sys.stdin.readline().rstrip()
    if ans == "Y":
        print("! 1")
        sys.exit(0)

