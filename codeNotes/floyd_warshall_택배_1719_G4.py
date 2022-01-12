import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
graph = [[float("inf")] * (N+1) for _ in range(N+1)]
paths = [[float("inf")] * (N+1) for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start][end] = cost
    graph[end][start] = cost
    paths[start][end] = end
    paths[end][start] = start

for k in range(1, N+1):
    graph[k][k] = 0
    paths[k][k] = float("inf")
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                paths[i][j] = k

for i in range(1, N+1):
    for j in range(1, N+1):
        print(paths[i][j] if paths[i][j] != float('inf') else "-", end = " ")
    print()
