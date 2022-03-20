# p.99 실전문제 04 - 1이 될 때까지

# 1. 입력
N, K = map(int, input().split())

# 2. N이 K로 나누어 지는지 여부의 따라 분기 처리
cnt = 0
while N > 1:
    if (N % K == 0):
        N //= K
    else:
        N -= 1
    cnt += 1

print(cnt)