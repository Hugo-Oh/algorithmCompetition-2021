import sys
import heapq as hq

sys.stdin=open("input.txt", "rt")
a, b = map(int, input().split())
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append([1, e])
    graph[e].append([1, s])

heap = []
heap.append([0, a])
distances = [float('inf') for _ in range(N+1)]
distances[a] = 0

while heap:
    cost, now = hq.heappop(heap)
    if cost > distances[now]:
        continue
    else:
        for w, v in graph[now]:
            distance = cost + w
            if distance < distances[v]:
                distances[v] = distance
                hq.heappush(heap, [distance, v])

print(distances[b] if distances[b] != float('inf') else -1)