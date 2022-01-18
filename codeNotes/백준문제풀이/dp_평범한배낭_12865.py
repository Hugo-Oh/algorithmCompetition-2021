import sys
sys.stdin = open("input.txt", "rt")
N, K = map(int, input().split())

# 1번방법 내가 아는 방법

# dp = [0 for _ in range(K+1)]
# for now in range(N):
#     now_weight, now_value = map(int, input().split())
#     for w in range(K, -1, -1):
#         if now_weight <= w:
#             dp[w] = max(dp[w], dp[w-now_weight] + now_value)
#
#
# print(dp[K])


# 2번방법 2차원 배열 사용(1번 사용)
dp = [[0] * (K+1) for _ in range(N+1)]

for now in range(1, N+1):
    now_weight, now_value = map(int, input().split())
    for w in range(1, K+1):
        if w >= now_weight:
            dp[now][w] = max(dp[now-1][w-now_weight] + now_value, dp[now-1][w])
        else:
            dp[now][w] = dp[now-1][w]

print(dp[N][K])
