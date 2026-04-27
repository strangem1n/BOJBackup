import sys
input = sys.stdin.readline

two_eight = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7"
}
n = input().rstrip()
ans = ""
while len(n) >= 3:
    ans = two_eight[n[-3:]] + ans
    n = n[:-3]
if len(n) == 0:
    print(ans)
else:
    if len(n) == 2:
        n = "0" + n
    else:
        n = "00" + n
    ans = two_eight[n] + ans
    print(ans)
