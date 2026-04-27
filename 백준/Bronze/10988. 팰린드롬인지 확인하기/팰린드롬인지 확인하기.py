word = list(input())
rev_word = word[:]
rev_word.reverse()
if word == rev_word:
    print(1)
else:
    print(0)