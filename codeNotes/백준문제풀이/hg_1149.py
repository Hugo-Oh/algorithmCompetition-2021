import sys
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input())
dp = [[0, 0, 0] for _ in range(N+1)] #[r, g, b]

distance = [list(map(int, input().split())) for _ in range(N)]


for i in range(1, N+1):




print(min(dp[N]))

# 완탐, dfs로 풀기 - 당연히 시간초과