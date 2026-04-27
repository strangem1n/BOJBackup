def pizza(person, showerbooth, time, money):
    get = 0
    for _ in range(person // showerbooth):
        get += showerbooth * money
        money -= time
        if money <= 0:
            return get
    get += (person % showerbooth) * money
    return get


n, m, t, k = map(int, input().split())
print(pizza(n, m, t, k))
