import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(M)]
distances = [[float("inf")] * N for _ in range(M)]
distances[0][0] = 0
visited = [[False] * N for _ in range(M)]
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]

heap = []
hq.heappush(heap, [0, 0, 0])
visited.append([0, 0])
while heap:
    cost, now_y, now_x = hq.heappop(heap)
    if [now_y, now_x] == [M-1, N-1]:
        print(distances[now_y][now_x])
        break

    if cost > distances[now_y][now_x]:
        continue

    else:
        for dy, dx in zip(ny, nx):
            next_y, next_x = now_y + dy, now_x + dx
            if 0 <= next_y < M and 0 <= next_x < N and visited[next_y][next_x] is False:
                visited[next_y][next_x] = True
                if graph[next_y][next_x] == 0:
                    distances[next_y][next_x] = cost
                    hq.heappush(heap, [cost, next_y, next_x])
                elif graph[next_y][next_x] == 1:
                    distances[next_y][next_x] = cost + 1
                    hq.heappush(heap, [cost + 1, next_y, next_x])