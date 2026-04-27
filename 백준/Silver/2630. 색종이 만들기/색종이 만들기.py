import sys
input = sys.stdin.readline

class MakeColorPaper:
    def __init__(self):
        self.white = 0
        self.blue = 0

    def cutpaper(self, num, array):
        initial = array[0][0]
        if num == 1:
            if initial == 0:
                self.white += 1
            else:
                self.blue += 1
        else:
            for i in range(num):
                for j in range(num):
                    if array[i][j] != initial:
                        num = num // 2
                        array1 = [array[r][0:num] for r in range(num)]
                        array2 = [array[r][num:] for r in range(num)]
                        array3 = [array[r][0:num] for r in range(num, num * 2)]
                        array4 = [array[r][num:] for r in range(num, num * 2)]
                        self.cutpaper(num, array1)
                        self.cutpaper(num, array2)
                        self.cutpaper(num, array3)
                        self.cutpaper(num, array4)
                        return None
            if initial == 0:
                self.white += 1
            else:
                self.blue += 1

    def countpaper(self):
        print(self.white)
        print(self.blue)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = MakeColorPaper()
result.cutpaper(N, arr)
result.countpaper()
