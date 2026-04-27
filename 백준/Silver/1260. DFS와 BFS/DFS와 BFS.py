# DFS: 깊이 내려가는 경로 순서로 출력하는 것이 조건
# 스택에 넣을 때마다 연결된 점이 있는지 계속 확인하면서 내려가기 때문에 스택에 넣을 때마다 출력
def dfs(k):
    stack = [0] * n
    visited = [0] * (n+1)    # 방문 여부 기록
    top = 0
    stack[top] = k    # 시작지점을 스택에 넣음
    print(k, end=" ")  # 맨 처음 시작지점 출력
    visited[k] = 1
    while top > -1:    # 스택이 빌 때까지 반복
        start = stack[top]    # 스택의 top에서 하나 꺼냄
        if len(adj[start]) > 0:    # 뽑은 정점과 연결된 정점이 있으면
            for j in range(len(adj[start])):    # 연결된 지점 하나씩 확인
                end = adj[start][j]
                if visited[end] == 0:    # 이전에 방문하지 않았으면
                    visited[end] = 1    # 방문 기록
                    top += 1
                    stack[top] = end    # 스택의 top에 집어넣기
                    print(end, end=" ")  # 방문 성공했으니 출력
                    break    # 더 깊이 내려가기 위해 반복 종료
            else:    # 연결된 점이 모두 방문 기록이 있으면 이 지점 탐색 실패.
                top -= 1    # 스택에서 하나 더 꺼내기 위해 top 하나 빼기
        else:    # 뽑은 정점과 연결된 곳이 없어도 탐색 실패이니 top 하나 빼기
            top -= 1


# BFS: 한 지점에 연결된 지점을 나란히 출력하는 것이 조건
# 큐에서 하나씩 뽑아서 그 지점과 연결된 지점을 큐에 넣기 때문에 큐에서 뽑을 때마다 출력
def bfs(k):
    q = [0] * n
    visited = [0] * (n+1)    # 방문 여부 기록
    front = rear = 0    # 큐의 출구 / 입구
    q[rear] = k    # 시작지점을 큐에 넣음
    rear += 1    # 큐의 길이 1 증가
    visited[k] = 1
    while front != rear:    # 큐가 빌 때까지 반복
        start = q[front]   # 큐의 front에서 하나 뽑음
        print(start, end=" ")
        front += 1    # 다음에 큐에서 뽑을 지점
        if len(adj[start]) > 0:    # 뽑은 정점과 연결된 정점이 있으면
            for j in range(len(adj[start])):    # 연결된 지점 하나씩 확인
                end = adj[start][j]
                if visited[end] == 0:    # 이전에 방문하지 않았으면
                    visited[end] = 1    # 방문 기록
                    q[rear] = end    # 큐의 rear에 집어넣기
                    rear += 1    # 큐의 길이 1 증가


n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]    # 이 리스트의 인덱스를 출발지점, 내부 리스트의 요소가 연결된 도착지점으로 한다.
for i in range(m):    # 간선의 개수만큼 반복
    s, e = map(int, input().split())
    if e not in adj[s]:    # 두 정점 사이에 간선이 여러 개 있을 수 있으니, 중복된 간선은 제거한다.
        adj[s].append(e)
    if s not in adj[e]:    # 간선이 양방향으로 연결되었으니 출발지점과 도착지점을 맞바꿔서 한 번 더 기록
        adj[e].append(s)
for i in range(n+1):    # 정점 번호가 작은 것부터 방문해야 해서 도착지점을 모은 리스트를 정렬한다.
    adj[i].sort()

dfs(v)    # 탐색 결과가 공백 하나를 두고 출력됨
print("")    # 줄 바꿈
bfs(v)
