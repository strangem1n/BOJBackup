import sys
avg = 0
total = 0

for _ in range(20):
    sub, point, grade = sys.stdin.readline().split()
    if grade == "A+":
        avg += float(point) * 4.5
    elif grade == "A0":
        avg += float(point) * 4.0    
    elif grade == "B+":
        avg += float(point) * 3.5
    elif grade == "B0":
        avg += float(point) * 3.0
    elif grade == "C+":
        avg += float(point) * 2.5
    elif grade == "C0":
        avg += float(point) * 2.0
    elif grade == "D+":
        avg += float(point) * 1.5
    elif grade == "D0":
        avg += float(point) * 1.0
    elif grade == "F":
        avg += float(point) * 0
    
    if grade != "P":
        total += float(point)
    else:
        pass    

print(avg/total)