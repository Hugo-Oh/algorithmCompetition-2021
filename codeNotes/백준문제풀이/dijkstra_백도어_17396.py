import sys
import heapq as hq
sys.stdin = open('input.txt', "rt")

N, M = map(int, input().split())
watched = list(map(int, input().split()))
heap = []
graph = [[] for _ in range(N)]
distances = [float('inf') for _ in range(N)]
distances[0] = 0
watched[N-1] = 0

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([c, e])
    graph[e].append([c, s])
hq.heappush(heap, [0, 0])

while heap:
    now_cost, now = hq.heappop(heap)
    if now_cost > distances[now]:
        continue
    else:
        for next_cost, next_node in graph[now]:
            distance = now_cost + next_cost
            if distance < distances[next_node] and not watched[next_node]:
                distances[next_node] = distance
                hq.heappush(heap, [distance, next_node])


print(distances[N-1] if distances[N-1] != float("inf") else -1)
