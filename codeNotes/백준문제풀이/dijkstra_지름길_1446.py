import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")
N, D = map(int, input().split())

graph = [[[1, i+1]] for i in range(100001)]

heap = []
heap.append([0, 0])

for _ in range(N):
    s, e, cost = map(int, input().split())
    graph[s].append([cost, e])
distances = [float('inf') for _ in range(100001)]
distances[0] = 0

while heap:
    cost, cur = hq.heappop(heap)
    if cost > distances[cur]:
        continue
    if cur == D:
        print(cost)
        break
    else:
        for post_cost, post in graph[cur]:
            distance = cost + post_cost
            if post <= D and distance < distances[post]:
                distances[post] = distance
                hq.heappush(heap, [distance, post])