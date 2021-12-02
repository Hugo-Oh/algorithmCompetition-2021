import sys
sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    array = [[0] + list(map(int, input().split())) for _ in range(2)]

    dp = [[0, 0] for _ in range(N+1)]
    dp[0] = [array[0][1], array[1][1]]
    for now in range(N+1):
        dp[now][0] = max(array[0][now] + dp[now-1][1], dp[now-1][0])
        dp[now][1] = max(array[1][now] + dp[now-1][0], dp[now-1][1])

    print(max(dp[N]))
