import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [arr[0] for _ in range(N+1)]




for now in range(N+1):
    for before in range(now):
        if arr[now] > arr[before]:
            dp[now] = max(dp[now], dp[now] + arr[before])

print(dp)
