import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
result = []
for i in range(8):
    result.append(int(a[i]))
    result.append(int(b[i]))

while len(result) != 2:
    new_result = []
    for i in range(len(result)-1):
        new_result.append((result[i]+result[i+1])%10)
    result = new_result

for r in result:
    print(r, end="")
