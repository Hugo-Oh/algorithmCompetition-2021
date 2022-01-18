import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N, M, K, X = map(int ,input().split())
q = []
graph = [[] for _ in range(N+1)]
distances = [float('inf')] * (N+1)
hq.heappush(q, [0, X])
distances[X] = 0

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append([1, e])

while q:
    c, v = hq.heappop(q)
    if c > distances[v]:
        continue

    else:
        for nc, nv in graph[v]:
            distance = c + nc
            if distance < distances[nv]:
                distances[nv] = distance
                hq.heappush(q, [distance, nv])

if K not in distances:
    print(-1)

for i in range(1, N+1):
    if distances[i] == K:
        print(i)
