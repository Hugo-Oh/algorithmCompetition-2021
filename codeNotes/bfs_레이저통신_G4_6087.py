import sys
from collections import deque

# sys.stdin = open("input.txt", "rt")

W, H = map(int, input().split())

graph = [list(map(str, input())) for _ in range(H)]


C_lst = []

for i in range(W):
    for j in range(H):
        if graph[j][i] == "C":
            C_lst.extend([j, i])
            graph[j][i] = float("inf")
        if graph[j][i] == ".":
            graph[j][i] = float('inf')




s_y, s_x, t_y, t_x = C_lst
q = deque()
q.append([s_y, s_x])
graph[s_y][s_x] = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    graph[s_y][s_x] = 0
    y, x, = q.popleft()
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        while True:

            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                break

            if graph[ny][nx] == "*":
                break

            if graph[ny][nx] < graph[y][x] + 1:
                break

            graph[ny][nx] = graph[y][x] + 1
            q.append([ny, nx])
            ny += dy[k]
            nx += dx[k]


print(graph[t_y][t_x] - 1)












