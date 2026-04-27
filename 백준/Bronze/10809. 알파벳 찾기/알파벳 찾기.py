aList = []
for i in range(ord('a'), ord('z')+1):
    aList.append(chr(i))

indexList = []

word = input()

for i in aList:
    indexList.append(word.find(i))

print(*indexList)