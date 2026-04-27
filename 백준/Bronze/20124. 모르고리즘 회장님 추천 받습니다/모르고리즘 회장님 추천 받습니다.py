import sys
input = sys.stdin.readline

n = int(input())
people = []
cnt = 0
for _ in range(n):
    name, num = input().split()
    num = int(num)
    if cnt < num:
        people = [name]
        cnt = num
    elif cnt == num:
        people.append(name)
people.sort()
print(people[0])
