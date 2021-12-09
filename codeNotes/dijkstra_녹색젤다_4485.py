import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")
index = 1
while True:
    N = int(input())
    if N == 0:
        break

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    distances = [[float('inf')] * N for _ in range(N)]
    heap = []

    distances[0][0] = graph[0][0]
    hq.heappush(heap, [graph[0][0], 0, 0])

    while heap:
        cost, y, x = hq.heappop(heap)
        if cost > distances[y][x]:
            continue
        if (y, x) == (N-1, N-1):
            print(f"Problem {index}: {cost}")
            break
        else:
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] is False : #기저 1
                    distance = cost + graph[ny][nx]

                    if distance < distances[ny][nx]:
                        distances[ny][nx] = distance
                        visited[ny][nx] = True
                        hq.heappush(heap, [distance, ny, nx])
    index += 1