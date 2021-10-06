import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for now in range(N):
    for before in range(now):
        if arr[now] > arr[before]:
            dp[now] = max(dp[now], dp[before] + 1)

print(max(dp))