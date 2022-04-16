def find_one(ls):
    new_ls = []
    for i in ls:
        new_ls.append(i+1)
        new_ls.append(i*2)
        new_ls.append(i*3)
        new_ls.append(i*5)
    return set(new_ls)

X = int(input())
ls = [1]
cnt = 0

while True:
    ls = find_one(ls)
    cnt += 1

    if X in ls:
        print(cnt)
        break
