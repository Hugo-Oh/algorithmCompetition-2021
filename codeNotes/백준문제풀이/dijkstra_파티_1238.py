import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([cost, e])

def dijkstra(start, end):
    distances = [float('inf') for _ in range(N + 1)]
    heap = []
    hq.heappush(heap, [0, start])
    distances[start] = 0

    while heap:
        w, v = hq.heappop(heap) #위치확인!
        if w > distances[v]:
            continue
        else:
            for ww, vv in graph[v]:
                distance = w + ww
                if distance < distances[vv]:
                    distances[vv] = distance
                    hq.heappush(heap, [distance, vv])
    return distances[end]


maxx = -float('inf')
for i in range(1, N+1):
    temp = dijkstra(i, X) + dijkstra(X, i)
    if temp > maxx:
        maxx = temp

print(maxx)


