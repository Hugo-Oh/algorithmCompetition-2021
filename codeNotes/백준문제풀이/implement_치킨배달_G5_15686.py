import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())

def bfs(y, x, opt = 1):
    visited = [[-1] * N for _ in range(N)]
    visited[y][x] = 0

    q = deque()
    q.append([y, x])

    while q:
        y, x = q.popleft()
        if graph[y][x] == opt:
            ans.append(visited[y][x])


        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])

# declare
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
home_li = []
ans = []

# init
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home_li.append([i, j])

ans_li = []
for y, x in home_li:
    bfs(y, x)
    print(ans)
    ans_li.append([sum(ans), y, x])
    ans = []

ans_li.sort()
print(ans_li[:M])

