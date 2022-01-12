import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            graph[i][j] = -1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

idx = 1
ans_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == -1:import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            graph[i][j] = -1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

idx = 1
ans_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == -1:
            num = 1
            q = deque([[i, j]])
            graph[i][j] = idx

            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == -1:
                        graph[ny][nx] = graph[y][x]
                        q.append([ny, nx])
                        num += 1

            ans_list.append(num)
            idx += 1

print(idx-1)
ans_list.sort()
for c in ans_list:
    print(c)
            num = 1
            q = deque([[i, j]])
            graph[i][j] = idx

            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == -1:
                        graph[ny][nx] = graph[y][x]
                        q.append([ny, nx])
                        num += 1

            ans_list.append(num)
            idx += 1

print(idx-1)
ans_list.sort()
for c in ans_list:
    print(c)
