padoban = [1, 1, 1, 2, 2]
for i in range(95):
    a = padoban[i] + padoban[i+4]
    padoban.append(a)

t = int(input())
for _ in range(t):
    n = int(input())
    print(padoban[n-1])