import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

#방향그래프
T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())

    distances = [float("inf") for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    q = []

    for _ in range (D):
        e, s, cost = map(int, input().split())
        graph[s].append([cost, e])

    distances[C] = 0
    hq.heappush(q, [0, C])
    maxx_time = 0
    while q:
        w, v = hq.heappop(q)
        if w > distances[v]:
            continue
        else:
            for ww, vv in graph[v]:
                distance = w + ww
                if distance < distances[vv]:
                    distances[vv] = distance
                    hq.heappush(q, [distance, vv])

    cnt = sum([1 for x in distances if x != float('inf')])
    maxx_time = [x for x in distances if x != float('inf')]
    print(cnt, max(maxx_time))
