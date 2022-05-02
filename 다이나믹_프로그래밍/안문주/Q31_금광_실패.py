# t = int(input())
t = 2
# n, m = map(int, input().split())
n, m = 4, 4
# gold_ls = list(map(int, input().split()))
gold_ls = list(map(int, '1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2'.split()))
golds = []

for i in range(n):
    g_ls = []
    for j in range(m):
        idx = (i*m) + j
        g_ls.append(gold_ls[idx])
    golds.append(g_ls)

print(golds)

max_sum_gold = 0
j = 0

while j != m:
    gl_max = [golds[i][j] for i in range(n)]

    if j == 0:
        max_idx = gl_max.index(max(gl_max))
        max_num = max(gl_max)
        max_sum_gold += max_num
        print(f'j : {j}, max_idx = {max_idx}, max_num = {max_num}, max_sum_gold = {max_sum_gold}')
        print('gl_max :', gl_max)
        j += 1

    else:
        move_ls = [max_idx - 1, max_idx, max_idx + 1]
        max_idx = gl_max.index(max(gl_max))
        max_num = max(gl_max)

        if max_idx in move_ls:
            max_sum_gold += max_num
            print(f'j : {j}, max_idx = {max_idx}, max_num = {max_num}, move_ls = {move_ls}, max_sum_gold = {max_sum_gold}')
            print('gl_max :', gl_max)
            j += 1

        else:
            golds[max_idx][j] = 0
            gl_max[j] = 0

            print(f'j : {j}, max_idx = {max_idx}, max_num = {max_num}, move_ls = {move_ls}, max_sum_gold = {max_sum_gold}')
            print('gl_max :', gl_max)

            print('????????????')
            # j += 1

print(max_sum_gold)