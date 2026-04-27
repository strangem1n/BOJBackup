class stack:
    def __init__(self):
        self.stack = []

    def push(self, X):
        self.stack.append(X)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0
        
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1
        
a = stack()
n = int(input())
for _ in range(n):
    order = str(input())
    if 'push' in order:
        order, n = order.split()
        n = int(n)
        a.push(n)
    elif order == 'pop':
        print(a.pop())
    elif order == 'size':
        print(a.size())
    elif order == 'empty':
        print(a.empty())
    elif order == 'top':
        print(a.top())