n = int((input()))
dic = set()
for _ in range(n):
    a = str(input())
    dic.add(a)
dic = list(dic)

dic.sort(key=lambda x: (len(x), x))

for i in dic:
    print(i)