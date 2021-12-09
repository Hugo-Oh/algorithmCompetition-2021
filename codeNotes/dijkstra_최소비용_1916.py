import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N = int(input())
E = int(input())

graph = [[] for _ in range(N+1)]

distances = [float('inf') for _ in range(N+1)]

for _ in range(E):
    S, E, C = map(int, input().split())
    graph[S].append([E, C])

start, target = map(int, input().split())

heap = []
distances[start] = 0
heap.append([0, start])

while heap:
    now_cost, now = hq.heappop(heap)
    if now_cost > distances[now]:
        continue
    if now == target:
        print(distances[target])
    else:
        for next, next_cost in graph[now]:
            distance = distances[now] + next_cost
            if distance < distances[next]:
                distances[next] = distance
                hq.heappush(heap, [distance, next])



