# p.92 실전문제 02 - 큰 수의 법칙

# 1. 입력
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

# 2. 내림차순 정렬
data.sort(reverse = True)

# print("count\t val")
# 3. 연속 K번, M번 더하기
cnt = 0
val = 0
while cnt < M:
    for i in range(K):
        val += data[0]

    val += data[1]
    cnt += (K+1)
    # print(count,"\t\t",val)

print(val)