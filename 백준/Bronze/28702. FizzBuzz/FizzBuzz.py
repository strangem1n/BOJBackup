a = input()
b = input()
c = input()

try:
    a = int(a)
    check = 1
except:
    pass

try:
    b = int(b)
    check = 2
except:
    pass

try:
    c = int(c)
    check = 3
except:
    pass

ans = 0

if check == 1:
    ans = a + 3
elif check == 2:
    ans = b + 2
elif check == 3:
    ans = c + 1

if ans % 3 == 0 and ans % 5 == 0:
    print('FizzBuzz')
elif ans % 3 == 0:
    print('Fizz')
elif ans % 5 == 0:
    print('Buzz')
else:
    print(ans)