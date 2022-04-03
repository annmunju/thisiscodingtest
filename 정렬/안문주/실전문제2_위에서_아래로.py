# 하나의 수열에는 다양한 수가 존재한다. 이 수를 큰수부터 작은수의 순서로 정렬. 내림차순으로 정렬하는 프로그램 만들기
ls = list()
n = int(input())
for _ in range(n):
    ls.append(int(input()))

result = sorted(ls, reverse=True)

for r in result:
    print(r, end=' ')