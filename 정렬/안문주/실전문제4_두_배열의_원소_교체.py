n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sort_a = sorted(a)
sort_b = sorted(b, reverse=True)


for i in range(n):
    k -= 1
    if sort_a[i] < sort_b[i]:
        sort_a[i], sort_b[i] = sort_b[i], sort_a[i]
    if k == 0 or sort_a[i] >= sort_b[i]:
        break

print(sum(sort_a))