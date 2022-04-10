n, c = map(int, input().split())
ls = [int(input()) for _ in range(n)]

ls.sort()

new_ls = [0 for _ in range(ls[-1]+1)]

for i in ls:
    new_ls[i] = 1

print(ls)
print(new_ls)
print(ls[0], ls[-1], ls[n//3 * 1], ls[n//3 * 2])

