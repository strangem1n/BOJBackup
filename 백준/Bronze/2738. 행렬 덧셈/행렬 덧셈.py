mat1 = []
mat2 = []
n, m = map(int, input().split())

if n and m > 0:
    while True:
        try:
            for _ in range(n):
                temp1 = list(map(int, input().split()))
                while len(temp1) > m:
                    temp1.pop()
                mat1.append(temp1)


            for _ in range(n):
                temp2 = list(map(int, input().split()))
                while len(temp2) > m:
                    temp2.pop()
                mat2.append(temp2)

            break

        except EOFError:
            break

for i in range(n):
    for j in range(m):
        mat1[i][j] += mat2[i][j]

for k in range(n):
    print(*mat1[k])