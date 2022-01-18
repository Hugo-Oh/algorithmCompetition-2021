import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

paths = [[float("inf")] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
distances = [[float("inf")] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])
    graph[end].append([cost, start])
    paths[start][end] = end
    paths[end][start] = start

for i in range(1, N+1):
    q = []
    hq.heappush(q, [0, i])
    distances[i][i] = 0

    while q:
        w, v = hq.heappop(q)
        if w > distances[i][v]:
            continue

        for ww, vv in graph[v]:
            distance = w + ww
            if distance < distances[i][vv]:
                distances[i][vv] = distance
                hq.heappush(q, [distance, vv])
                paths[vv][i] = v

for i in range(1, N+1):
    for j in range(1, N+1):
        # print(paths[i][j] , end = " " if paths[i][j] != float("inf") else "-")
        print(paths[i][j] if paths[i][j] != float("inf") else "-", end=" ")
    print()