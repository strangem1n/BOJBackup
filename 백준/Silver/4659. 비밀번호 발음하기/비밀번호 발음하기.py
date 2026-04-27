import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input().rstrip()
    if pw == 'end':
        break

    if 'a' not in pw and 'e' not in pw and 'i' not in pw and 'o' not in pw and 'u' not in pw:
        print(f"<{pw}> is not acceptable.")
        continue
        
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1] and pw[i] != 'e' and pw[i] != 'o':
            print(f"<{pw}> is not acceptable.")
            break
        if i < len(pw)-2:
            if pw[i] in vowel and pw[i+1] in vowel and pw[i+2] in vowel:
                print(f"<{pw}> is not acceptable.")
                break
            elif pw[i] not in vowel and pw[i+1] not in vowel and pw[i+2] not in vowel:
                print(f"<{pw}> is not acceptable.")
                break
    else:
        print(f"<{pw}> is acceptable.")
