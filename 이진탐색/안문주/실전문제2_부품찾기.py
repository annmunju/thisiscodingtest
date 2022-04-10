n = int(input())
all_ls = list(map(int, input().split()))
m = int(input())
find_ls = list(map(int, input().split()))

def find_part(ls, num, start, end):
    while start <= end:
        mid = (end + start) // 2
        if ls[mid] == num:
            return True
        elif ls[mid] > num:
            end = mid-1
        else:
            start = mid+1
    return False

sort_ls = sorted(all_ls)
# set 집합 자료형 이용하면 보다 빠르게 연산 가능할듯!

for part in find_ls:
    result = find_part(sort_ls, part, 0, n-1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')
