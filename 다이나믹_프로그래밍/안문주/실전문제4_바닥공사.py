def find_one(ls):
    new_ls = []
    for i in ls:
        new_ls.append(i+2)
        new_ls.append(i+4)
        new_ls.append(i+4)
    return new_ls

n = int(input())
ls = [2, 4, 4]
all_ls = [2, 4, 4]

for i in range(1, 4):
    new_ls = find_one(ls)
    all_ls.extend(new_ls)

print(all_ls)
print(all_ls.count(2*n))
