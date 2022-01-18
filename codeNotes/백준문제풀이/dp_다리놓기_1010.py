import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    ## 서로 겹쳐질 수 없다


    dp =  [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if i > j:
                continue
            if i == j:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    answer = dp[N-1][M-1]
    print(answer)