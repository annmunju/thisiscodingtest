from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
ls = list(map(int, input().split()))

if bisect_right(ls, x) == n:
    print(-1)
else :
    print(bisect_right(ls, x) - bisect_left(ls, x))