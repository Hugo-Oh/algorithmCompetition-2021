import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

def dijkstra(heaps):
    while heap:
        cost, now_y, now_x = hq.heappop(heap)
        if cost > distances[now_y][now_x]: #기저조건 1
            continue
        if (now_y, now_x) == (t_y, t_x): #종결조건
            print(cost)
            break

        else:
            for k in range(4):
                ny = now_y + dy[k]
                nx = now_x + dx[k]
                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] is False:
                    visited[ny][nx] = True
                    if graph[ny][nx] == "0":
                        hq.heappush(heap, [cost, ny, nx])
                        distances[ny][nx] = cost

                    else:
                        hq.heappush(heap, [cost + 1, ny, nx])
                        distances[ny][nx] = cost + 1

N, M = map(int, input().split())
s_y, s_x, t_y, t_x = map(lambda x: int(x) - 1, input().split())
graph = [list(input()) for _ in range(N)]
distances = [[float('inf')] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 초기화시키기

heap = []
heap.append([0, s_y, s_x])
visited[s_y][s_x] = True
distances[s_y][s_x] = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dijkstra(heap)