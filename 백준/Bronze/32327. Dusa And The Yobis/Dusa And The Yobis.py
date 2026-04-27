import sys
dusa = int(sys.stdin.readline())
while True:
    yobi = int(sys.stdin.readline())
    if dusa > yobi:
        dusa += yobi
    else:
        print(dusa)
        break