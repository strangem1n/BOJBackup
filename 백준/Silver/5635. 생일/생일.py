n = int(input())
old = [12, 31, 2010]
old_name = None
young = [1, 1, 1990]
young_name = None
for _ in range(n):
    name, *birthday = input().split()
    birthday = list(map(int, birthday))
    if old[2] > birthday[2]:
        old = birthday
        old_name = name
    elif old[2] == birthday[2] and old[1] > birthday[1]:
        old = birthday
        old_name = name
    elif old[2] == birthday[2] and old[1] == birthday[1] and old[0] > birthday[0]:
        old = birthday
        old_name = name

    if young[2] < birthday[2]:
        young = birthday
        young_name = name
    elif young[2] == birthday[2] and young[1] < birthday[1]:
        young = birthday
        young_name = name
    elif young[2] == birthday[2] and young[1] == birthday[1] and young[0] < birthday[0]:
        young = birthday
        young_name = name

print(young_name)
print(old_name)