import sys
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input())
dp = [[0, 0, 0] for _ in range(N+1)] #[r, g, b]

distance = [list(map(int, input().split())) for _ in range(N)]
distance.insert(0, [0, 0, 0])

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1] + distance[i][0], dp[i-1][2] + distance[i][0])
    dp[i][1] = min(dp[i-1][0] + distance[i][1], dp[i-1][2] + distance[i][1])
    dp[i][2] = min(dp[i-1][0] + distance[i][2], dp[i-1][1] + distance[i][2])

print(min(dp[N]))

# 완탐, dfs로 풀기 - 당연히 시간초과