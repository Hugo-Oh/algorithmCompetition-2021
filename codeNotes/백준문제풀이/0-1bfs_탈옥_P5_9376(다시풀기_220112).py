import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

H, W = map(int, input().split())
graph = [list(input()) for _ in range(H)]
distances = [[float("inf")] * W for _ in range(H)]

q = deque()
criminal = []
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[2] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if graph[i][j] == "$":
            criminal.append([0, i, j])


for p in criminal:
    _, y, x = p
    distances[y][x] = 0
    q.append([0, y, x])
answer = []
print(q)
while q:
    cost, y, x = q.popleft()
    print(y, x, q)
    if cost > distances[y][x]:
        continue
    if y == 0 or x == 0 or y == H-1 or x == W - 1:
        answer.append(cost)

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < H and 0 <= nx < W and graph[ny][nx] != "*" and visited[ny][nx] != 0:
            visited[ny][nx] -= 2
            if distances[ny][nx] > cost:
                if graph[ny][nx] == ".":
                    q.appendleft([cost, ny, nx])
                    distances[ny][nx] = cost

                elif graph[ny][nx] == "#": # graph[ny][nx] == "#" 문인경우
                    q.appendleft([cost + 1, ny, nx])
                    distances[ny][nx] = cost + 1
                    graph[ny][nx] = "."



for i in range(H):
    for j in range(W):
        print(f"{distances[i][j]:>3}", end= " ")
    print()

for c in graph:
    print(c)

