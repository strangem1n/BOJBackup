import sys
sys.stdin.readline()
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
ints = A & B
Apart = A - ints
Bpart = B - ints
print(len(Apart)+len(Bpart))