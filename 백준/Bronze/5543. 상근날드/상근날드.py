import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(5)]
print(min(arr[:3]) + min(arr[3:]) - 50)