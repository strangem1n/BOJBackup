import sys
input = sys.stdin.readline

n = int(input())
word = input().rstrip()
arr = [0] * 10
for a in word:
    if a == "B":
        arr[0] += 1
    elif a == "R":
        arr[1] += 1
    elif a == "O":
        arr[2] += 1
    elif a == "N":
        arr[3] += 1
    elif a == "Z":
        arr[4] += 1
    elif a == "E":
        arr[5] += 1
    elif a == "S":
        arr[6] += 1
    elif a == "I":
        arr[7] += 1
    elif a == "L":
        arr[8] += 1
    elif a == "V":
        arr[9] += 1
arr[1] //= 2
arr[5] //= 2
print(min(arr))
