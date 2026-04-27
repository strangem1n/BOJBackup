result = 0
for _ in range(5):
    n = int(input())
    if n > 40:
        result += n
    else:
        result += 40
print(result//5)