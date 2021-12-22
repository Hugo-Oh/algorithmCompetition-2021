import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([cost, e])

A, B = map(int ,input().split())

def dijkstra(start, end):
    distances = [float('inf') for _ in range(N + 1)]
    paths = [-1 for _ in range(N + 1)]
    heap = []
    distances[start] = 0
    hq.heappush(heap, [0, start])

    while heap:
        w, v = hq.heappop(heap)
        if w > distances[v]:
            continue

        else:
            for ww, vv in graph[v]:
                distance = w + ww
                if distance < distances[vv]:
                    distances[vv] = distance
                    paths[vv] = v
                    hq.heappush(heap, [distance, vv])

    return distances[end], paths
pathresult = [B]
cost, paths = dijkstra(A, B)

temp = B
while paths[temp] != -1:
    pathresult.append(paths[temp])
    temp = paths[temp]

print(cost)
print(len(pathresult))
print(" ".join(map(str, pathresult[::-1])))

