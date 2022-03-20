# p.313 기출문제 03 - 문자열 뒤집기

# 1. 입력 받기
S = list(map(int, list(input())))

# 2. 0 -> 1 또는 1 -> 0으로 변하는 기점 수 구하기
idx, cnt = 0, 0
while idx < len(S)-1:
    if S[idx] != S[idx+1]:
        cnt += 1
    idx += 1

# 3. 기점 수 / 2 출력? (0->1 또는 1->0 중 1택해서 바꾸면 되니까)
print(cnt // 2)