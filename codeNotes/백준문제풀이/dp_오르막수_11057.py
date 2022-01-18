import sys
sys.stdin = open("input.txt", "rt")
N = int(input())


dp = [[0] * 10 for _ in range(N+1)]

for i in range(N+1):
    for j in range(10):
        if i == 0:
            dp[i][j] = 1
        elif j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[N][9] % 10007)