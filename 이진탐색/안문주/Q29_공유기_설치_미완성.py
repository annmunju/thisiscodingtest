n, c = map(int, input().split())
ls = [int(input()) for _ in range(n)]

ls.sort()

def find_mid(ls, start, end):

    mid_val = (ls[start] + ls[end]) // 2

    while start < end:
        mid_idx = (start + end) // 2

        if ls[mid_idx] == mid_val:
            return mid_idx
        elif ls[mid_idx] < mid_val:
            start = mid_idx+1
        else:
            end = mid_idx-1

    return mid_idx-1

# mid_idx = find_mid(ls, 0, n-1)
print(ls)
# print(mid_idx, ls[mid_idx])

if c == 2:
    result = ls[n-1] - ls[0]

# 1번째 시도
c -= 2
update_idx = find_mid(ls, 0, n-1)
print(ls[update_idx])
# 왼쪽
new_left_ls = ls[0:update_idx+1]
new_left_idx = find_mid(new_left_ls, 0, len(new_left_ls)-1)
print(new_left_ls[new_left_idx])
# 오른쪽
new_right_ls = ls[update_idx:n-1]
new_right_idx = find_mid(new_right_ls, 0, len(new_right_ls)-1)
print(new_right_ls[new_right_idx])






