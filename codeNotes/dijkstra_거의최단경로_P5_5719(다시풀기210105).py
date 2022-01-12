import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")


def dijkstra_path(start, end):
    q = []
    distances = [float('inf') for _ in range(N)]
    distances[start] = 0
    hq.heappush(q, [0, start])  # 초기값
    paths = [[] for _ in range(N)]
    paths[start].append(-1)

    while q:
        w, v = hq.heappop(q)
        if w > distances[v]:
            continue

        else:
            for ww, vv in graph_rev[v]:
                distance = ww + w # v노드까지의 기존 가중치합 + vv노드까지의 가중치
                if distance < distances[vv]:
                    distances[vv] = distance
                    hq.heappush(q, [distance, vv])
                    if paths[vv]: #비어있지 않으면
                        paths[vv].pop()
                    paths[vv].append(v)
    print(distances)
    print(paths)


N, M = map(int, input().split()) # 노드, 간선
S, D = map(int, input().split()) # 출발점, 도착점
graph = [[] for _ in range(N)]
graph_rev = [[] for _ in range(N)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])
    graph_rev[end].append([cost, start])

dijkstra_path(6, 0)




