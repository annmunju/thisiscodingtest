import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드개수 간선개수 입력
n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    # a 노드에서 b노드로 가는 거리가 1라는 의미
    a,b = map(int, input().split())
    graph[b].append((a, 1))
    graph[a].append((b, 1))

x,k = map(int, input().split())

def dijkstra(start):
    # 우선순위 큐
    q = []
    heapq.heappush(q, (0, start)) # 자기 자신으로 가는 최단 경로는 0
    distance[start] = 0

    while q: # 큐가 비어질때까지
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

company_to_k = []
for i in range(1, n+1):
    if distance[i] == INF:
        company_to_k.append(-1)
    else:
        company_to_k.append(distance[i])

# print(company_to_k)
to_k = company_to_k[k-1]

distance = [INF] * (n + 1)
dijkstra(k)

k_to_x = []
for i in range(1, n+1):
    if distance[i] == INF:
        k_to_x.append(-1)
    else:
        k_to_x.append(distance[i])

to_x = k_to_x[x-1]
# print(k_to_x)

print(to_k+to_x)