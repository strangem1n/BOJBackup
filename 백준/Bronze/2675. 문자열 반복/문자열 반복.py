num = int(input())
for _ in range(num):
    a = input().split()
    newList = []
    n = int(a[0])
    word = str(a[1])
    for i in range(len(word)):
        newList.append(word[i] * n)
    print(''.join(newList))