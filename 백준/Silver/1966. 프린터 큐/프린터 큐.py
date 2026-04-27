import sys
from collections import deque
input = sys.stdin.readline

def printerqueue(n, idx, queue):
    cnt = 1    # 인쇄되는 순서 저장
    while n > 0:
        important = max(queue)    # 큐에서 가장 중요도가 높은지 확인
        left_pop = queue.popleft()    # 큐에서 가장 왼쪽 요소를 일단 뽑아봄
        if idx == 0 and left_pop == important:    # 뽑은 요소가 알아볼 문서인지, 맞다면 큐에서 가장 중요도가 높은지
            return cnt
        elif idx != 0 and left_pop == important:    # 알아볼 요소는 아니지만 중요도가 가장 높다면 큐에서 제거
            cnt += 1
            idx -= 1    # 인덱스 하나 왼쪽으로 당기기
            n -= 1    # 문서의 개수 줄어듦
        else:    # 중요도가 낮다면
            queue.append(left_pop)    # 뽑은 요소를 가장 오른쪽에 집어넣음
            if idx == 0:    # 뽑은 요소가 알아볼 문서이면 가장 오른쪽으로 표시
                idx = n - 1
            else:    # 아니면 단순히 인덱스 하나 왼쪽으로 당기기
                idx -= 1

T = int(input())
for _ in range(T):
    N, i = map(int, input().split())    # 프린터 대기열 큐의 길이와 알아볼 문서의 위치
    q = deque(list(map(int, input().split())))
    result = printerqueue(N, i, q)
    print(result)