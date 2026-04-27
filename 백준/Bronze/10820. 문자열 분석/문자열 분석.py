import sys
input = sys.stdin.readline
while True:
    try:
        word = input()
        if word[-1] == "\n":
            word = word[:-1]
        l = u = n = s = 0
        for w in word:
            if w == " ":
                s += 1
            elif w.isupper():
                u += 1
            elif w.islower():
                l += 1
            else:
                 n += 1
        print(l, u, n, s)
    except:
        break