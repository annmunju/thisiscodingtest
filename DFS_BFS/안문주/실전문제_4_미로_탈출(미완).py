n, m = map(int, input().split())
graph = [[0]] * (n+1)
graph[0] = graph[0] * (m+1)

for i in range(1, n+1):
    graph[i] = graph[i]+list(map(int, list(input())))

x, y = 1, 1

from collections import deque

# 우, 하, 좌, 상 순서
dx = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque()
    queue.append(x, y)

    while queue:
        x, y = queue.popleft()

        





