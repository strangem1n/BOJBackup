import sys
n = int(sys.stdin.readline())
if n**2 <= 10**8:
    print('Accepted')
else:
    print('Time limit exceeded')