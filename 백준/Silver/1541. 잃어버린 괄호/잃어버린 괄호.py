test = input().split('-')
for i in range(len(test)):
    test[i] = test[i].split('+')
for i in range(len(test)):
    if len(test[i]) == 1:
        test[i] = int(test[i][0])
    else:
        test[i] = sum(map(int, test[i]))
result = test[0]
for i in range(1, len(test)):
    result -= test[i]
print(result)