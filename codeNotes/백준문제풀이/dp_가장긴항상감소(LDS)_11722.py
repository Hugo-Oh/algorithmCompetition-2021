import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
array = [0] + list(map(int, input().split()))

dp = [1 for _ in range(N+1)]

for now in range(1, N+1):
    for before in range(now):
        if array[now] < array[before]:
            dp[now] = max(dp[now], dp[before] + 1)

print(max(dp))