import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
# 1 = 길
# 0 = 벽
distances = [[float('inf')] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
distances[0][0] = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = []
visited[0][0] = True
hq.heappush(q, [0, 0, 0])

while q:
    cost, y, x = hq.heappop(q)
    if y == N-1 and x == N-1:
        print(cost)
        break
    if cost > distances[y][x]:
        continue
    else:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] is False:
                visited[ny][nx] = True # 방문처리 일단 하고
                if graph[ny][nx] == 0: # 벽이면 가중치 + 1
                    distances[ny][nx] = cost + 1
                    hq.heappush(q, [cost + 1, ny, nx])
                else: # 벽이 아니라 길이면 그대로
                    distances[ny][nx] = cost
                    hq.heappush(q, [cost, ny, nx])