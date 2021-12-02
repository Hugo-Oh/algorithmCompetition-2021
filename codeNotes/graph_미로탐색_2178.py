import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
queue = deque([])
distances = [[1] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

queue.append((0, 0))

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

while queue:
    cur_y, cur_x = queue.popleft()
    if cur_y == N-1 and cur_x == M-1:
        print(distances[cur_y][cur_x])

    for dy, dx in zip(ny, nx):
        next_y = cur_y + dy
        next_x = cur_x + dx
        if 0 <= next_y < N and 0 <= next_x < M:
            if graph[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                visited[next_y][next_x] = 1
                queue.append((next_y, next_x))
                distances[next_y][next_x] = distances[cur_y][cur_x] + 1
