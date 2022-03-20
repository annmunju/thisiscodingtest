# p.96 실전문제 03 - 숫자 카드 게임

# 1. N, M 입력
N, M = map(int, input().split())

# 2. 각 행 입력의 최솟값 요소만 min_list에 저장
min_list = []
for i in range(N):
    temp = list(map(int, input().split()))
    min_list.append(min(temp))

# 3. 요소 중 가장 최댓값 출력
print(max(min_list))