n = int(input())

dp = list(map(int, input().split()))

num = 0

if n == 1:
    num = 1
else:
    for i in range(0, n-1):
        if (dp[i] <= dp[i+1]):
            num += 1
            # print(i)

print(num)