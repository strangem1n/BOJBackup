n = int(input())
num_list = list(map(int, input().split()))

for i in range(n):
    num = num_list[i]
    root_num = int(num ** 0.5)
    if num == (root_num ** 2):
        print(1, end=" ")
    else:
        print(0, end=" ")