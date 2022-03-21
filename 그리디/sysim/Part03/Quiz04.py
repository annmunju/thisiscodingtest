# p.314 기출문제 04 - 만들 수 없는 금액
from itertools import permutations

# 1. 입력 받기
N = int(input())
data = list(map(int, input().split()))

# 2. 최대 N개 까지 조합 하여 만들 수 있는 금액 구하기
total_list = set(data)
cnt = 2
while cnt <= N:
    temp_list = list(permutations(data, cnt))
    # print(cnt, "개씩 조합한 모든 경우(중복 제거):", set(temp_list))

    for i in range(len(temp_list)):
        total_list.add(sum(temp_list[i]))
    cnt += 1
# print("만들 수 있는 금액:", total_list)

# 3. 만들 수 없는 금액 출력
result = 1
while True:
    if result not in total_list:
        print(result)
        break
    result += 1
