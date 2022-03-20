# 입력 받기
n, m = map(int, input().split())
map = list()

for i in range(n):
    map.append(list(input()))

# 최종 결과값(아이스크림 개수) cnt, 최초 탐색 지점 (col, row) = (0, 0)
cnt = 0
col, row = 0, 0


# 지도에 0표시 -> 1표시로 전환
def check_map(map, col, row):
    if 0 <= col < n and 0 <= row < m and map[col][row] == '0':
        map[col][row] = '1'

        # 상하좌우도 0->1로 표시 전환
        check_map(map, col+1, row)
        check_map(map, col-1, row)
        check_map(map, col, row+1)
        check_map(map, col, row-1)

    # 지도 반환
    return map


# 지도에 0표시 지점 찾기
def find_zero(map, n, m):
    for col in range(n):
        for row in range(m):
            if map[col][row] == '0':
                # 0표시 찾으면 해당 col, row 반환
                return col, row
    # 0표시가 없으면 -1, -1 반환
    return -1, -1

# 이건 그냥 내가 지도좀 볼라고 ^^...
def print_map(map, n, m):
    for i in range(n):
        for j in range(m):
            print(map[i][j], end=' ')
        print()
    print()


# col 반환값 -1 될때까지 돌려돌려
while col != -1:
    # 0 지점 찾아서
    col, row = find_zero(map, n, m)
    # 해당 지점부터 지도 뒤집
    check_map(map, col, row)
    # 지도 보여줫
    print_map(map, n, m)

    # col -1 되면 세지말고 나머지 세줘
    if col != -1:
        cnt += 1


print(cnt)