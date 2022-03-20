# p.152 실전문제 04 - 미로탈출

N, M = map(int, input().split())
# print("세로:", N, "\t가로:", M)

# 1. 2차원 배열로 입력 저장
maze = []

for i in range(N):
    maze.append(list(map(int, input().split())))
# print(maze)
# print("x\t y\t count")

# 2. 미로 탈출
def escape(x,y,cnt):
    # print(x,"\t",y,"\t",cnt)
    if(x == N-1 and y == M-1): return cnt # 좌표가 출구이면 탈출!
    if(y == M-1 and x < N): return escape(x+1, y, cnt+1) # 가로 마지막 인덱스일 때 아래로 좌표 이동
    if(x == N-1 and x < M): return escape(x, y+1, cnt+1) # 세로 마지막 인덱스일 때 오른쪽으로 좌표 이동

    if(maze[x][y+1] == 0):
        return escape(x+1, y, cnt+1)
    else:
        return escape(x,y+1,cnt+1)

print("result: ", escape(0, 0, 1))