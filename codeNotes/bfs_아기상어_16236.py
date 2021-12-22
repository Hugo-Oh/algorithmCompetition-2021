import sys
import heapq as hq
from collections import deque
sys.stdin = open("input.txt", "rt")

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def findStart():
    for y in range(N):
        for x in range(N):
            if graph[y][x] == 9:
                return y, x

def findTarget(size):
    for y in range(N):
        for x in range(N):
            if 0 < graph[y][x] < size:
                return y, x


def shark(second, size):
    if not(any(any(0 < y < size for y in x) for x in graph)):
        print("done")
        return second, size

    s_y, s_x = findStart()
    t_y, t_x = findTarget(size)
    print(t_y, t_x)

    distances = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((s_y, s_x))


    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # initializing
    visited[s_y][s_x] = True
    distances[s_y][s_x] = 0


    while q:
        now_y, now_x = q.popleft()
        if (now_y, now_x) == (t_y, t_x):
            break

        for k in range(4):
            ny, nx = now_y + dy[k], now_x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] is False and graph[ny][nx] <= size:
                visited[ny][nx] = True
                distances[ny][nx] = distances[now_y][now_x] + 1
                q.append((ny, nx))



    graph[t_y][t_x] = 9
    graph[s_y][s_x] = 0
    second += distances[t_y][t_x]
    size += 1

    shark(second + distances[t_y][t_x], size + 1)


print(shark(0, 2))
for c in graph:
    print(c)


