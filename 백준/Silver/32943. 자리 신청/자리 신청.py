import sys
input = sys.stdin.readline

student, seat, log = map(int, input().split())
logs = [list(map(int, input().split())) for _ in range(log)]
logs.sort(key=lambda x: x[0])

seats = [0] * (seat + 1)
students = [0] * (student + 1)


for time, want_seat, want_student in logs:
    if seats[want_seat] == 0:
        if students[want_student] != 0:
            old_seat = students[want_student]
            seats[old_seat] = 0
        seats[want_seat] = want_student
        students[want_student] = want_seat

for idx, student in enumerate(students):
    if student == 0:
        continue
    print(idx, student)
