import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
K = int(input())

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

heap = []

distances = [float('inf') for _ in range(V+1)]
distances[K] = 0
heap.append([0, K])

while heap:
    now_cost, now = hq.heappop(heap)
    if now_cost > distances[now]:
        continue
    else:
        for next, next_cost in graph[now]:
            distance = now_cost + next_cost
            if distance < distances[next]:
                distances[next] = distance
                hq.heappush(heap, [distance, next])


for i in distances[1:]:
    print(i if i != float("inf") else "INF")