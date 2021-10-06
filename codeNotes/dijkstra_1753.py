import sys
import heapq
# input = sys.stdin.readline
sys.stdin = open("input.txt", "rt")

V, E = map(int, input().split())

S = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])


def dijkstra(g, start):
    distances = [float("inf")] * (V+1)
    distances[start] = 0
    q = list()
    q.append([0, start])

    while q:
        now_c, now_n = heapq.heappop(q)

        if now_c > distances[now_n]:
            continue

        for next_n, next_c in g[now_n]:
            distance = now_c + next_c
            if distance < distances[next_n]:
                distances[next_n] = distance
                heapq.heappush(q, [distance, next_n])

    return distances


ans_list = dijkstra(graph, S)
for i in range(1, V+1):
    print(ans_list[i]) if ans_list[i] != float('inf') else print("INF")
