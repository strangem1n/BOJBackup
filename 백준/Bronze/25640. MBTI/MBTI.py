mbti = input()
result = 0
n = int(input())
for _ in range(n):
    friend = input()
    if mbti == friend:
        result += 1
print(result)