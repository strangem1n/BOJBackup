import sys
input = sys.stdin.readline

n = int(input())
prefer = input().rstrip()

b = s = a = 0
for i in range(n):
    if prefer[i] == "B":
        b += 1
    elif prefer[i] == "S":
        s += 1
    else:
        a += 1

max_prefer = max(b, s, a)
result = ""
if max_prefer == b:
    result += "B"
if max_prefer == s:
    result += "S"
if max_prefer == a:
    result += "A"
if len(result) == 3:
    result = "SCU"
    
print(result)