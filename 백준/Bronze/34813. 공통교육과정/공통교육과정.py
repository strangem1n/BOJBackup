import sys
n = sys.stdin.readline()
if n[0] == "E":
    print("Exploration")
elif n[0] == "V":
    print("Veritas")
elif n[0] == "C":
    print("Claves")
else:
    print("Foundation")
