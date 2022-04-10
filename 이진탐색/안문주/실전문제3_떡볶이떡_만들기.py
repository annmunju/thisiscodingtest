n, m = map(int, input().split())
Dducks = list(map(int, input().split()))

max_num = max(Dducks)

def dduck_cut(ls, sum_num):
    dduck_ls = [x-sum_num if x-sum_num > 0 else 0 for x in ls]
    return sum(dduck_ls)

def find_num(ls, num, start, end):
    while start <= end:
        mid = (end + start) // 2
        if dduck_cut(ls, mid) == num:
            return mid
        elif dduck_cut(ls, mid) < num:
            end = mid-1
        else:
            start = mid+1
    return mid

print(find_num(Dducks, m, 0, max_num))