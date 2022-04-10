from bisect import bisect_left, bisect_right

ls = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

left_idx = bisect_left(ls, 4)
right_idx = bisect_right(ls, 4)

print(left_idx, ls[left_idx])
print(right_idx-1, ls[right_idx-1])
print(right_idx-left_idx)