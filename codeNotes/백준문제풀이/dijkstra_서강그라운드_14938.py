import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(R):
    s, e, length = map(int, input().split())
    graph[s].append([length, e])
    graph[e].append([length, s])


def dijkstra(start):
    q = []
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    q.append([0, start])

    while q:
        w, v = hq.heappop(q)
        if w > distances[v]:
            continue

        else:
            for ww, vv in graph[v]:
                distance = ww + w
                if distance < distances[vv]:
                    distances[vv] = distance
                    hq.heappush(q, [distance, vv])
    return distances[1:]

maxx = 0

for i in range(1, N+1):
    distances = dijkstra(i)
    answer = sum([1 * items[i] for i in range(N) if distances[i] <= M])
    if answer > maxx:
        maxx = answer

print(maxx)
