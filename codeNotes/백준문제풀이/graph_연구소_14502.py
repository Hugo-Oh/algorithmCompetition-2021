import sys
from itertools import combinations
from collections import deque
import copy
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

blank = []
queue = deque()
visited = []

for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            blank.append((y, x))
        if graph[y][x] == 2:
            queue.append((y, x))
            visited.append((y, x))

wall = combinations(blank, 3)
nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]
answer = 0

for combi in wall:
    graph_2 = [x[:] for x in graph]

    for y, x in combi:
        graph_2[y][x] = 1

    while queue:
        cur_y, cur_x = queue.popleft()

        for dy, dx in zip(ny, nx):
            next_y, next_x = cur_y + dy, cur_x + dx
            if 0 <= next_y < N and 0 <= next_x < M and (next_y, next_x) not in visited:
                if graph_2[next_y][next_x] == 0:
                    graph_2[next_y][next_x] = 2
                    visited.append((next_y, next_x))
                    queue.append((next_y, next_x))

    temp = sum(1 for row in graph_2 for x in row if x == 0)
    visited = []
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 2:
                queue.append((y, x))
                visited.append((y, x))

    if temp > answer:
        answer = temp

print(answer)