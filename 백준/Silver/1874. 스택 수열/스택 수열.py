class Arr:
    top = -1
    used = 0
    idx = 0

    def __init__(self, n):
        self.stack = [0] * n
        self.result = [''] * (n * 2)

    def push_or_pop(self, want):
        if want > self.used:
            for i in range(self.used+1, want+1):
                self.top += 1
                self.stack[self.top] = i
                self.used += 1
                self.result[self.idx] = '+'
                self.idx += 1
            self.result[self.idx] = '-'
            self.top -= 1
            self.idx += 1
        else:
            if self.stack[self.top] == want:
                self.top -= 1
                self.result[self.idx] = '-'
                self.idx += 1
            else:
                return 'NO'

    def answer(self):
        return self.result


N = int(input())
s = Arr(N)
for _ in range(N):
    w = int(input())
    status = s.push_or_pop(w)
    if status == 'NO':
        print(status)
        break
else:
    answer = s.answer()
    for i in range(N*2):
        print(answer[i])
