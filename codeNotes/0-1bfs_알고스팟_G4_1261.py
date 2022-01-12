import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
q = deque()
q.appendleft([0, 0])
visited[0][0] = True

while q:
    y, x = q.popleft()
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < M and 0 <= nx < N and visited[ny][nx] is False:
            visited[ny][nx] = True
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x]
                q.appendleft([ny, nx])
            else:
                graph[ny][nx] = graph[y][x] + 1
                q.append([ny, nx])

print(graph[M-1][N-1])