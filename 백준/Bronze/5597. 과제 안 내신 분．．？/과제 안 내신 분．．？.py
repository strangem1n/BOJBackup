import sys

students = []
for i in range(1, 31):
    students.append(i)

homework = list(map(int, sys.stdin.readlines()))
for i in homework:
    students.remove(i)

for i in range(len(students)):
    print(students[i])