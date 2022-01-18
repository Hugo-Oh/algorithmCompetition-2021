import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = []

first = []
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            first.append((y, x))

queue = deque()
queue.extend(first)
ny = [-1, 1, 0, 0]
nx = [0, 0, 1, -1]

while queue:
    cur_y, cur_x = queue.popleft()
    for dy, dx in zip(ny, nx):
        next_y, next_x = cur_y + dy, cur_x + dx
        if 0 <= next_y < N and 0 <= next_x < M:
            if graph[next_y][next_x] == 0:
                queue.append((next_y, next_x))
                graph[next_y][next_x] = graph[cur_y][cur_x] + 1

ans = 0

for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            print(-1)
            sys.exit(0)
        if ans < graph[y][x]:
            ans = graph[y][x]

print(ans - 1)
