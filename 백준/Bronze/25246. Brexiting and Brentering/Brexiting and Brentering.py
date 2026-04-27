word = input()
for i in range(len(word)-1, -1, -1):
    if word[i] in ['a', 'e', 'i', 'o', 'u']:
        print(word[:i+1] + 'ntry')
        break
