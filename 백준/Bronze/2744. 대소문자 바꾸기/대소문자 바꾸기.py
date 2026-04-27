text = list(input())
reverse = []
for i in text:
    if i.isupper() is True:
        j = i.lower()
        reverse.append(j)
    else:
        j = i.upper()
        reverse.append(j)
print(''.join(reverse))