import sys, math
input = sys.stdin.readline

q = 1000000007
a = int(input())
x = int(input())
l = int(math.log2(x))
memo = [a%q]
for i in range(l):
    memo.append((memo[-1]**2)%q)
ans = 1
binary = str(bin(x))[2:][::-1]
for i in range(l+1):
    if binary[i] == "1":
        ans *= memo[i]
        ans %= q
print(ans)
