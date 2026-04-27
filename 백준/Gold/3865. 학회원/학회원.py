import sys
input = sys.stdin.readline

def get_n(org_name):
    temp = set()
    for person in info[org_name]:
        if info.get(person):
            if memo.get(person):
                temp = temp.union(memo[person])
            else:
                another_org = get_n(person)
                memo[person] = another_org
                temp = temp.union(another_org)
        else:
            temp.add(person)
    return temp

while True:
    n = int(input())
    if n == 0:
        break
    info = {}
    memo = {}
    first_org = None
    for _ in range(n):
        org, people = input().split(":")
        if not first_org:
            first_org = org
        info[org] = people[:-2].split(",")
    print(len(get_n(first_org)))
