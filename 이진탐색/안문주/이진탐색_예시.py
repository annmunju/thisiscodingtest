from time import time

def binary_search(array, target, start, end):
    tm = time()
    if start > end:
        print(tm-time())
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        print(tm-time())
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


ls = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

n = 10
target = int(input())

print(binary_search(ls, target, 0, n-1))

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

print(binary_search2(ls, target, 0, n-1))