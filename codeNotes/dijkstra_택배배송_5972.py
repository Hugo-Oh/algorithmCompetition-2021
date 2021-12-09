import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([c, e])
    graph[e].append([c, s])

distances = [float('inf') for _ in range(N+1)]
distances[1] = 0
heap = []
heap.append([0, 1])

while heap:
    now_cost, now = hq.heappop(heap)
    if now == N:
        print(distances[now])
        break
    if now_cost > distances[now]:
        continue

    else:
        for next_cost, next_node in graph[now]:
            distance = now_cost + next_cost
            if distance < distances[next_node]:
                distances[next_node] = distance
                hq.heappush(heap, [distance, next_node])

