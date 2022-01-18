import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0 for _ in range(N+1)]
dp[1] = arr[1]

for now in range(2, N + 1):
    for before in range(now + 1):
        dp[now] = max(dp[now], dp[now - before] + arr[before])

print(dp[now])