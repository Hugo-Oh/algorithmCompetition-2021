import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())

dp = [[0] * X for X in range(1, N+2)]

for i in range(N+1):
    for j in range(i+1):
        if i == 0:
            dp[i][j] = 1
        if j == 0:
            dp[i][j] = 1
        elif j == i:
            dp[j][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[N][K] % 10007)
