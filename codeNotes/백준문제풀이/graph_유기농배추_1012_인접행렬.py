import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# 인접 행렬로풀
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    ny = [0, 0, 1, -1]
    nx = [1, -1, 0, 0]
    visited = []
    ans = 0

    def dfs(cur_y, cur_x):
        graph[cur_y][cur_x] = 0
        visited.append((cur_y, cur_x))

        for dy, dx in zip(ny, nx):
            next_y, next_x = cur_y + dy, cur_x + dx
            if 0 <= next_y < N and 0 <= next_x < M:  # base
                if (next_y, next_x) not in visited and graph[next_y][next_x] == 1:
                    dfs(next_y, next_x)

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                dfs(y, x)
                ans += 1

    print(ans)
