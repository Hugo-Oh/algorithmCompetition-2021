import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")
T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        start, end, c = map(int, input().split())
        graph[start].append([c, end])
        graph[end].append([c, start])
    candidates = [int(input()) for _ in range(t)]

    def dijkstra(start):
        q = []
        paths = [0 for _ in range(n+1)]
        paths[start] = -1
        hq.heappush(q, [0, start])
        distances = [float('inf') for _ in range(n+1)]
        distances[start] = 0

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
                        paths[vv] = v

        return paths

    def checkPath(end):
        path = ""
        temp = end

        while paths[temp] != -1:
            path += f"{temp}"
            temp = paths[temp]
            if paths[temp] == float('inf'):
                break

        path += f"{s}"
        if str(g) in path and str(h) in path:
             answer.append(end)

    answer = []
    paths = dijkstra(s)

    for end in candidates:
        checkPath(end)

    answer.sort()
    print(" ".join(map(str, answer)))
