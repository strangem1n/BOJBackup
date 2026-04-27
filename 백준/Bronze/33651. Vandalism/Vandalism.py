a = input()
uapc = ['U', 'A', 'P', 'C']

for i in a:
    for j in range(4):
        if i == uapc[j]:
            uapc[j] = ""
print("".join(uapc))