import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")
w, h = map(int, input().split())

graph = [list(map(str, input())) for _ in range(h)]

visited = [[[False for _ in range(4)] for _ in range(w)] for _ in range(h)]
print(visited)
distances = [[float('inf')] * w for _ in range(h)]
q = []
target = []

for i in range(h):
    for j in range(w):
        if graph[i][j] == "C":
           target.extend([i, j])

s_y, s_x, t_y, t_x = target
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q.append([0, s_y, s_x, 0])
q.append([0, s_y, s_x, 1])# 시작이니까 0
q.append([0, s_y, s_x, 2])# 시작이니까 0
q.append([0, s_y, s_x, 3])# 시작이니까 0

distances[s_y][s_x] = 0
visited[s_y][s_x][0] = True
visited[s_y][s_x][1] = True
visited[s_y][s_x][2] = True
visited[s_y][s_x][3] = True


while q:
    print(q)
    cost, y, x, d= hq.heappop(q)
    if cost > distances[y][x]:
        continue
    else:
        for nd in range(4):
            ny = y + dy[nd]
            nx = x + dx[nd]

            if 0 <= ny < h and 0 <= nx < w and visited[ny][nx][nd] is False and graph[ny][nx] != "*":
                visited[ny][nx][nd] = True

                if cost + 1 < distances[ny][nx]:
                    distances[ny][nx] = cost + 1
                    hq.heappush(q, [cost + 1 , ny, nx, nd])




for c in distances:
    print(c)