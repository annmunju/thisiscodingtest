n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(n-1, 0, -1):
    for j in range(i):
        left = dp[i][j] + dp[i-1][j]
        right = dp[i][j+1] + dp[i-1][j]
        dp[i-1][j] = max(left, right)

print(dp[0][0])