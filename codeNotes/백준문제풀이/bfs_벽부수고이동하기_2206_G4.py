import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[False, False]] * M for _ in range(N)]
distances = [[-1] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

s_y = 0
s_x = 0

q = deque()
q.append([s_y, s_x, 0,False])
visited[s_y][s_x] = [True, True]
distances[s_y][s_x] = 1

while q:
    y, x, cost, isCrashed = q.popleft()
    print(cost)
    if y == N-1 and x == M-1:
        print(cost)
        break

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < N and 0 <= nx < M: #방문한적없음
            if graph[ny][nx] == 0:
                if visited[ny][nx][0] is False and isCrashed is False: #무조건 이동 가능
                    visited[ny][nx][0] = True
                    print(cost)

                if visited[ny][nx][1] is False and isCrashed is True:
                    visited[ny][nx][1] = True
                    q.append([ny, nx, cost + 1, isCrashed])

            if graph[ny][nx] == 1 and visited[ny][nx][1] is False:
                if isCrashed is False:
                    visited[ny][nx][1] = True
                    q.append([ny, nx, cost + 1, True])
                    distances[ny][nx] = distances[y][x] + 1



