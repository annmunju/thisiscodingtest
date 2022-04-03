p = list(input())


def div_bracket(p, ls):
    left, right = 0, 0
    for i, a in enumerate(p):
        if a == '(':
            left += 1
        if a == ')':
            right += 1
        if left == right:
            u = p[:i + 1]
            ls.append(u)
            v = p[i + 1:]
            div_bracket(v, ls)
            return ls
    return p


def right_bracket(p):
    if p[0] == ')' or p[-1] == '(':
        p[0], p[-1] = '(', ')'
        for i, b in enumerate(p[1:-1]):
            print(i, b)
            if b == ')':
                p[i + 1] = '('
            if b == '(':
                p[i + 1] = ')'
    return p

def solution(p):
    p = list(p)

    brackets = []

    for ls in div_bracket(p, []):
        brackets.append(right_bracket(ls))

    ansLs = []
    for bracket in brackets:
        ans = ''.join(bracket)
        ansLs.append(ans)

    answer = ''.join(ansLs)
    return answer



print(solution(p))