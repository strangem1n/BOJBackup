import sys

def push(lis, X):
    lis.append(X)

def pop(lis):
    if len(lis) > 0:
        print(lis[0])
        del lis[0]
    else:
        print(-1)

def size(lis):
    return len(lis)

def empty(lis):
    if len(lis) == 0:
        return 1
    else:
        return 0
    
def front(lis):
    if len(lis) > 0:
        return lis[0]
    else:
        return -1
    
def back(lis):
    if len(lis) > 0:
        return lis[-1]
    else:
        return -1
    
a = []
n = int(sys.stdin.readline())

for _ in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        push(a, int(order[1]))
    elif order[0] == 'pop':
        pop(a)
    elif order[0] == 'size':
        print(size(a))
    elif order[0] == 'empty':
        print(empty(a))
    elif order[0] == 'front':
        print(front(a))
    elif order[0] == 'back':
        print(back(a))