a, b = map(int, input().split())
n = ""
while a > 0:
    r = a % b
    a = a // b

    if r >= 10:
        r = ord("A") + r - 10
        R = chr(r)
        n += R
    else:
        R = str(r)
        n += R

n_list = list(n)
n_list.reverse()
print("".join(n_list))