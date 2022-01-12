import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")
w, h = map(int, input().split())

graph = [list(map(str, input())) for _ in range(h)]

visited = [[[False for _ in range(4)] for _ in range(w)] for _ in range(h)]
distances = [[float('inf')] * w for _ in range(h)]
q = []
target = []

for i in range(h):
    for j in range(w):
        if graph[i][j] == "C":
           target.extend([i, j])

s_y, s_x, t_y, t_x = target
dx = [1, -1, 0, 0]
dy = [0, 0, -1, +1]
distances[s_y][s_x] = 0
hq.heappush(q, [0, s_y, s_x, 0])
hq.heappush(q, [0, s_y, s_x, 1])
hq.heappush(q, [0, s_y, s_x, 2])
hq.heappush(q, [0, s_y, s_x, 3])
visited[s_y][s_x][0] = True

while q:
    d, cost, y, x = hq.heappop(q)


    for nd in range(4):
        ny = y + dy[nd]
        nx = x + dx[nd]
        print(q, y, x, d)
        if 0 <= ny < h and 0 <= nx < w and visited[ny][nx][nd] is False and graph[ny][nx] != "*":
            visited[ny][nx][nd] = True

            if d == nd and cost < distances[ny][nx]:
                distances[ny][nx] = cost
                hq.heappush(q, [nd, cost, ny, nx, ])

            elif d != nd and cost + 1 < distances[ny][nx]:
                hq.heappush(q, [nd, cost + 1, ny, nx, ])
                distances[ny][nx] = cost + 1

for i in range(h):
    for j in range(w):
        print(distances[i][j] if distances[i][j] != float("inf") else "*", end=" ")
    print()
print()

