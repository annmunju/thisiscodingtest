from sys import stdin

n = int(stdin.readline())
houses = list(map(int, stdin.readline().split()))
houses.sort()

# 최소값과 그 최소값 idx reset
min = sum(houses)
min_idx = n+1

# 중간값(중위수값)부터 작아지는 순으로 최소값 update
for i in range(houses[int(len(houses)/2)], 0, -1):
    distance = 0
    # 전체를 돌면서 거리의 합 구하기
    for j in houses:
        distance += abs(j-i) #절대값
    # 현 지점의 거리 합이 min값보다 작거나 같으면 업데이트
    if distance <= min:
        min = distance
        min_idx = i
    # 현 지점의 거리 합이 min보다 크면 그만.
    else :
        break

print(min_idx)
