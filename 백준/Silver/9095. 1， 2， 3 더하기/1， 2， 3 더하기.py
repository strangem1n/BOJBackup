def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (f(n-1) + f(n-2) + f(n-3))
    
t = int(input())
for _ in range(t):
    print(f(int(input())))
