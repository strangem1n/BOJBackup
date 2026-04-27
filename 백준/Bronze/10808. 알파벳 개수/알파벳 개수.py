arr = [0] * 26
word = input()
for i in word:
    arr[ord(i)-97] += 1
print(*arr)