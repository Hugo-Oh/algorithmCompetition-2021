import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

M, N = map(int, input().split())

graph = [[] for _ in range(N+1)]

for s in range(1, N+1):
    wall = list(map(int, input()))
    for e in range(1, M+1):
            graph[s].append([e, 1])
        else:
            graph[s].append([e, 0])
        if wall[e-1] == 1:

for r in graph:
    print(r)

distances = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
distances.insert(0, [])
q = []
q.append([1, 1, 0])
distances[1][1] = 0
visit = [[0] for _ in range(M+1) for _ in range(N+1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
while q:
    cur_x, cur_y, cur_c = hq.heappop(q)
    if cur_c > distances[cur_x][cur_y]:
        continue
    for nx, ny in zip(dy, dx):
        next_x = cur_x + nx
        next_y = cur_y + ny
        if 0 <= next_x < N and 0 <= next_y <= M and visit[next_x][next_y] == 0:
            if graph[next_y][next_x] == 1:
                hq.heappush(q, [next_y, next_x, cur_c + 1])
            else:
                hq.heappush(q, [next_y, next_x, cur_c])
            visit[next_y][next_x] = 1


for r in graph:
    print(r)

print(distances)