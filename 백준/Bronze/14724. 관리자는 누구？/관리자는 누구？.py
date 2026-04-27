import sys
input = sys.stdin.readline

n = int(input())
club = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
max_problem = max_idx = 0
for i in range(9):
    max_person = max(map(int, input().split()))
    if max_problem < max_person:
        max_problem = max_person
        max_idx = i
print(club[max_idx])
