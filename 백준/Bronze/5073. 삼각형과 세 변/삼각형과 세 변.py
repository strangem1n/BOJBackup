while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break
    elif a + b <= c or a + c <= b or b + c <= a:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a != b and b != c and a != c:
        print("Scalene")
    else:
        print("Isosceles")