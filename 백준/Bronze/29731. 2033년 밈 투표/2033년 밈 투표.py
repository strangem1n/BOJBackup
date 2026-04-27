import sys
input = sys.stdin.readline

meme = ["Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]

n = int(input())
chk = True
for _ in range(n):
    sen = input().rstrip()
    if sen not in meme:
        chk = False
if chk:
    print("No")
else:
    print("Yes")
