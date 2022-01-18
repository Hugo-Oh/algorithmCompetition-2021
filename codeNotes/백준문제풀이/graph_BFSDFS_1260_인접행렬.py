import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N, M, V = map(int, input().split())

# 인접행렬
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    r, c = map(int,input().split())
    graph[r][c] = 1
    graph[c][r] = 1

visit = [0 for _ in range(N+1)]
stack = [V]
 visit[V] = 1

# 1. DFS
while stack:
    cur = stack.pop()
    temp = []
    if visit[cur] == 0:
        print(cur, end=" ")
        visit[cur] = 1


    for next_node in range(1, N+1):
        if graph[cur][next_node] == 1 and visit[next_node] == 0:
            temp.append(next_node)
    temp.sort(reverse = True)
    stack += temp


# BFS
print()
queue = deque([V])
visit = [0 for _ in range(N+1)]
visit[V] = 1
while queue:
    cur = queue.popleft()
    print(cur, end=" ")
    for next_node in range(1, N+1):
        if graph[cur][next_node] == 1 and visit[next_node] == 0:
            visit[next_node] = 1
            queue.append(next_node)
