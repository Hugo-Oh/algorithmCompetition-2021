import sys
sys.stdin = open("input.txt", "rt")
N = int(input())
dp = [x for x in range(N+1)]

for n in range(1, N+1):
    for i in range(1, n):
        if i * i > n:
            break
        else:
            dp[n] = min(dp[n-(i*i)] + 1, dp[n])

print(dp)