n = int(input())
ls = list(map(int, input().split()))

idx = 0
while True:
    if ls[idx] >= 0 :
        break
    idx += 1

def find_idx(ls, start, end):
    while start <= end:
        mid = (start + end) // 2
        if ls[mid] == mid:
            return mid
        elif ls[mid] > mid:
            end = mid-1
        else:
            start = mid + 1
    return -1

print(find_idx(ls, idx, n-1))
