import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n,k=map(int, input().split())

graph=[]



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
data=[]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j, 0))
S, X, Y = map(int, input().split())
data.sort()
queue=deque(data)

while queue:
    virus, x, y, second = queue.popleft()
    if second == S:
        break

    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx>=n or ny>=n or nx<0 or ny<0:
            continue

        if graph[nx][ny] != 0:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            queue.append((graph[nx][ny], nx, ny, second + 1))

print(S)
for c in graph:
    print(c)
print(graph[X-1][Y-1])

