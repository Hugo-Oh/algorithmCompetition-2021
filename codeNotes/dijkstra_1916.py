import sys
import heapq as hq
#sys.stdin = open("input.txt", "rt")


def dijkstra(g, start, end):
    distances = [float('inf')] * (N+1)
    distances[start] = 0
    q = list()
    q.append([0, start])

    while q:
        cur_c, cur_n = hq.heappop(q)
        if cur_c > distances[cur_n]:
            continue

        for next_n, next_c in g[cur_n]:
            distance = next_c + cur_c
            if distance < distances[next_n]:
                distances[next_n] = distance
                hq.heappush(q, [distance, next_n])

    return distances[end]


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])

S, E = map(int, input().split())
print(dijkstra(graph, S, E))
