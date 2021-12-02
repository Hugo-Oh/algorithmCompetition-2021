import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = []

def dfs(cur_node):
    visited.append(cur_node)
    for next_node in graph[cur_node]:
        if next_node not in visited:
            dfs(next_node)


answer = 0
for node in range(1, N+1):
    if node not in visited:
        dfs(node)
        answer += 1

print(answer)

"""graph = [[0] * (N+1) for _ in range(N+1)]

answer = 0
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

visited = []

def dfs(curnode):
    visited.append(curnode)

    for nextnode in range(1, N+1):
        if graph[curnode][nextnode] == 1 and nextnode not in visited:
            graph[curnode][nextnode] = 0
            dfs(nextnode)


for y in range(1, N+1):
    for x in range(1, N+1):
        if graph[y][x] == 1:
            dfs(y)
            answer += 1

print(answer)"""
