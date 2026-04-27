groups, problems = map(int, input().split())
memory = {}
for i in range(groups):
    name = input()
    number = int(input())
    members = []
    for j in range(number):
        member = input()
        members.append(member)
    memory[name] = members

for x in range(problems):
    problem = input()
    check = int(input())
    if check == 0:
        result = memory.get(problem)
        result.sort()
        for y in result:
            print(y)
    elif check == 1:
        for check_group, check_list in memory.items():
            if problem in check_list:
                print(check_group)