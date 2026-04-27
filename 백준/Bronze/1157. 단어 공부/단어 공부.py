word = input().upper()
alphabet = []
freq = []

for i in range(26):
    alphabet.append(chr(ord("A")+i))

for i in alphabet:
    freq.append(word.count(i))

if freq.count(max(freq)) == 1:
    print(alphabet[freq.index(max(freq))])
else:
    print("?")