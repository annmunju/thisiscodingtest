n = int(input())
dc = dict()
for _ in range(n):
    name, score = input().split()
    dc[name] = int(score)

sort_values = sorted(dc.items(), key=lambda x:x[1])

for val in sort_values:
    print(val[0], end=' ')