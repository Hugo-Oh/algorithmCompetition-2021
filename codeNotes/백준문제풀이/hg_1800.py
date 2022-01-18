import sys
import heapq
sys.stdin = open("input.txt", "rt")


N, P, K = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(P):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
    graph[end].append([start, cost])

distance = [float('inf') for _ in range(N+1)]
distance[1] = 0
q = []
q.append([0, 1])


def dijkstra():
    while q:
        cur_c, cur_n = heapq.heappop(q)
        if distance[cur_n] < cost:
            continue
        for next_n, next_c in graph[cur_n]:
            dist = cur_c + next_c

            if dist < distance[next_n]:
                print(dist, next_n)
                distance[next_n] = dist
                heapq.heappush(q, [dist, next_n])

            if next_n == N:
                print(distance)
                for _ in range(K+1):
                    answer = heapq.heappop(q)


print(dijkstra())
