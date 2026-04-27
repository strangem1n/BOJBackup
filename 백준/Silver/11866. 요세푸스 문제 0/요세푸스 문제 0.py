n, k = map(int, input().split())
queue = [i for i in range(1, n+1)]
result = [0] * n
idx = 0
front = -1
while idx < n:
    for _ in range(k):
        front += 1
        front = front % n
        if queue[front] == 0:
            while queue[front] == 0:
                front += 1
                front = front % n
    result[idx] = str(queue[front])
    idx += 1
    queue[front] = 0
print("<" + ", ".join(result) + ">")
