import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N, M, K = map(int, input().split())

q = []
distances = [[float('inf')] * K for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
distances[1][0] = 0 #시작점 기준 자기자신 0
hq.heappush(q, [0, 1]) #start = 1 = 시작도시

for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([cost, e])


while q:
    w, v = hq.heappop(q)
    for ww, vv in graph[v]:

        distance = w + ww

        if distance < distances[vv][K-1]:
            distances[vv][K-1] = distance #그냥 이렇게 안하고 무조건 append한 다음에 sort가능
            distances[vv].sort() # 넣고 흔드는 과정이 중요
            hq.heappush(q,[distance, vv])

ans = [x[K-1] for x in distances][1:]
for i in ans:
    print(i if i != float('inf') else -1)