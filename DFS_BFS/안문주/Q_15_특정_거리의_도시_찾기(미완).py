n, m, k, x = map(int, input().split())
graph = list()
find_map = [[]] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    find_map[a] = find_map[a] + (list([b]))

def find_X_k(graph, x):
    # 처음 함수 실행했을때
    cnt_map = [0] * (n + 1)

    # graph[x] 에 숫자가 있으면
    if len(graph[x]) > 0:
        for i in graph[x]:
            cnt_map[i] += 1

    return cnt_map

print(find_X_k(graph, x))