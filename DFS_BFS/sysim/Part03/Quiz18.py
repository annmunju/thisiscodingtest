# p.346 기출문제 18 - 괄호 변환

def pToUnV(s):
    temp_list = list(s)
    left, right = 0, 0
    for i in range(len(temp_list)):
        if temp_list[i] == '(':
            left += 1
        else:
            right += 1

        if (left == right):
            return i+1

def solution(p):
    # 1. 입력이 빈 문자열인 경우 return
    if p == '':
        return p

    answer = ''
    # 2. [균형잡힌 괄호 문자열] u, v로 나누기
    idx = pToUnV(p)
    u = p[:idx]
    v = p[idx:]
    # print("u:", u, "\t\t|v:", v)

    if u.index(')') == 0: # u의 첫번째 요소가 '(' 으로 [올바른 괄호 문자열]이 아닌 경우
        # 문제의 4.의 과정을 해야함
        answer = '(' + solution(v) + ')'
        u_list = list(u)
        u_list.pop(0)    # u의 첫번째 요소 제거
        u_list.pop()     # u의 마지막 요소 제거
        for i in u_list:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    else:
        answer += (u + solution(v))

    return answer