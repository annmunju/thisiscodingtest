from time import time

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

start = time()
print(fibo(99))
print(time()-start)

# 같은 함수 여러번 호출로 중복되기 때문에 시간 복잡도는 O(2^N) : 매우 높은 시간 복잡도

d = [0] * 100

def fibo_top_down(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

start = time()
print(fibo_memo(99))
print(time()-start)

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

start = time()
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i + 2]

print(time() - start)
print(d[n])