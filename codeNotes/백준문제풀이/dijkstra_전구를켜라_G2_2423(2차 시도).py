import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

M, N = map(int, input().split())
graph = [list(f"{input()}") for _ in range(M)]

q = []
paths = [[[] for _ in range(N+1)] for _ in range(M+1)]

for i in range(M):
    for j in range(N):
        if graph[i][j] == "/":
            paths[i][j].append([1, i+1, j+1])
            paths[i+1][j+1].append([1, i, j])
            paths[i+1][j].append([0, i, j+1])
            paths[i][j+1].append([0, i+1, j])

        else:
            paths[i][j].append([0, i+1, j+1])
            paths[i+1][j+1].append([0, i, j])
            paths[i+1][j].append([1, i, j+1])
            paths[i][j+1].append([1, i+1, j])


hq.heappush(q, *paths[0][0])
distances = [[float("inf")] * (N+1) for _ in range(M+1)]
distances[0][0] = 0


while q:
    cost, y, x = hq.heappop(q)
    if cost > distances[y][x]:
        continue

    else:
        for w, ny, nx in paths[y][x]:
            distance = cost + w
            if 0 <= ny < M+1 and 0 <= nx < N+1:
                if distance < distances[ny][nx]:
                    distances[ny][nx] = distance
                    hq.heappush(q, [distance, ny, nx])

if (M + N) % 2 == 0:
    print(distances[M][N])
else:
    print("NO SOLUTION")