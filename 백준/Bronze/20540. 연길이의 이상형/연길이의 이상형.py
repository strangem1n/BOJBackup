import sys
mbti = sys.stdin.readline().rstrip()
if mbti[0] == "I":
    print("E", end="")
else:
    print("I", end="")
if mbti[1] == "N":
    print("S", end="")
else:
    print("N", end="")
if mbti[2] == "F":
    print("T", end="")
else:
    print("F", end="")
if mbti[3] == "P":
    print("J", end="")
else:
    print("P", end="")
