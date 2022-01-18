import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    s, e, cost = map(int, input().split())
    graph[s].append([cost, e])
    graph[e].append([cost, s])
v1, v2 = map(int, input().split())

# 무조건 1번 노드와 N번 노드 사이에 두 노드를 지난다.
def dijkstra(start, end):
    distances = [float('inf') for _ in range(N + 1)]
    heap = []
    hq.heappush(heap, [0, start])
    distances[start] = 0
    while heap:
        w, v = hq.heappop(heap)
        if w > distances[v]:
            continue
        if v == end:
            return w

        else:
            for ww, vv in graph[v]:
                distance = w + ww
                if distance < distances[vv]:
                    distances[vv] = distance
                    hq.heappush(heap, [distance, vv])
    return False

one_to_v1 = dijkstra(1, v1)
v1_to_v2 = dijkstra(v1, v2)
v2_to_N = dijkstra(v2, N)

one_to_v2 = dijkstra(1, v2)
v2_to_v1 = v1_to_v2
v1_to_N = dijkstra(v1, N)

answer = min(one_to_v1+v1_to_v2+v2_to_N, one_to_v2+v2_to_v1+v1_to_N)
print(answer if answer != False else -1)

