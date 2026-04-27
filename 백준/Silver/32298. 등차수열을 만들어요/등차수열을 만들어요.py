import sys
import math
input = sys.stdin.readline

def prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if not dic[i] and num % i == 0:
            return True
    return False

dic = {k: False for k in range(1, 2000001)}
dic[1] = True
for k in range(2, 2000001):
    if prime(k):
        dic[k] = True
        continue

n, m = map(int, input().split())
for k in range(1, 2000001):
    if dic.get(k) and dic[k]:
        temp = [k]
        dic[k] = False
        for j in range(1, n):
            chk = k + m * j
            if dic[chk]:
                temp.append(chk)
                dic[chk] = False
            else:
                break
        else:
            print(*temp)
            break
else:
    print(-1)