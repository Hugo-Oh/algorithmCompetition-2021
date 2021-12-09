import sys
sys.stdin = open("input.txt", "rt")
N = int(input())
dp = [0 for _ in range(N+1)]

dp[1] = 0
dp[2] = 3

for i in range(2, N+1):
    dp[i] = dp[i-2] * dp[i-2]
)

print(dp[1:])