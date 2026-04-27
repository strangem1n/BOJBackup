a = int(input())
n = 0
bee = 1
while bee < a:
    n += 1
    bee += 6 * n
print(n+1)