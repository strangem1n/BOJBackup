dial = {}
time = 0
word = input()

for i in range(6):
    dial[chr(ord("A")+ i * 3)] = i + 3
    dial[chr(ord("B")+ i * 3)] = i + 3
    dial[chr(ord("C")+ i * 3)] = i + 3
dial["S"] = 8
for i in range(2):
    dial[chr(ord("T")+ i * 3)] = i + 9
    dial[chr(ord("U")+ i * 3)] = i + 9
    dial[chr(ord("V")+ i * 3)] = i + 9
dial["Z"] = 10

for i in range(len(word)):
    chr = word[i]
    time += dial.get(chr)

print(time)