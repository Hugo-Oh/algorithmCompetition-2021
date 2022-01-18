import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")

a, b = map(int, input().split())
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
dist = [float('inf') for _ in range(N+1)]
dist[1] = 0
q = []

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append([e, 1])
    graph[e].append([s, 1])

q.append((0, a))

while q:
    cur_cost, cur_node = hq.heappop(q)
    for next_node, next_cost in graph[cur_node]:

        next_co = cur_cost + next_cost
        if cost[next_node] > next_co:
            cost[next_cost] = next_cost
            hq.heappush(q, (next_co, next_node))

        if next_node == e:
            print(next_co)
            sys.exit(0)

print(cost)




