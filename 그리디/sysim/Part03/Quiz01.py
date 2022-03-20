# p.311 기출문제 01 - 모험가 길드

# 1. 입력 받기
N = int(input())
data = list(map(int, input().split()))

# 2. 인덱스, 그룹 수, 미포함 모험가 수
idx, cnt, uncnt = 0, 0, 0

# 3. 내림차순 정렬
data.sort(reverse=True)

# 4. 인덱스 내의 그룹 수 구하기
while idx < N:
    # 공포도가 남아있는 모험가 수보다 클 때 pass
    if(data[idx] > (N-uncnt)):
        idx += 1
        uncnt += 1
        pass

    # 공포도 크기의 그룹 생성
    cnt += 1
    idx += data[idx]

print(cnt)