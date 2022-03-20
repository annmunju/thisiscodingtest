# p.312 기출문제 02 - 곱하기 혹은 더하기

# 1. 입력 받기
S = list(map(int, list(input())))

# 2. 0이 아니면 곱하기
idx, val = 0, 0
while idx < len(S):
    if(val == 0):
        val += S[idx]
    else:
        val *= S[idx]
    idx += 1

print(val)