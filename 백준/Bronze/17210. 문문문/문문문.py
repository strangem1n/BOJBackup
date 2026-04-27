n = int(input())
a = int(input())
b = abs(a-1)

if n > 5:
    print("Love is open door")
else:
    for i in range(n-1):
        if i % 2 == 0:
            print(b)
        else:
            print(a)