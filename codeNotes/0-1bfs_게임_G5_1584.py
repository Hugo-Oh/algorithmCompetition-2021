import sys
from collections import deque
sys.stdin = open("input.txt", "rt")


# input & declare
graph = [[0] * 501 for _ in range(501)]
visited  = [[False] * 501 for _ in range(501)]

N = int(input())
# 위험한 지역
for _ in range(N):
    s_x, s_y, e_x, e_y = map(int, input().split())

    if s_x == e_x and s_y == e_y:
        graph[s_y][s_x] = 1
    else:
        if s_x > e_x:
            s_x, e_x = e_x, s_x
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        for i in range(s_y, e_y+1):
            for j in range(s_x, e_x+1):
                graph[i][j] = 1

M = int(input())
# 죽음의 지역
for _ in range(M):
    s_x, s_y, e_x, e_y = map(int, input().split())
    if s_x == e_x and s_y == e_y:
        graph[s_y][s_x] = float("inf")
    else:
        if s_x > e_x:
            s_x, e_x = e_x, s_x
        if s_y > e_y:
            s_y, e_y = e_y, s_y

        for i in range(s_y, e_y+1):
            for j in range(s_x, e_x+1):
                graph[i][j] = float("inf")


q = deque()
s_y, s_x = 0, 0
q.appendleft([0, s_y, s_x])
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited[0][0] = True

while q:
    cost, y, x = q.popleft()
    if y == 500 and x == 500:
        print(cost)
        break

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < 501 and 0 <= nx < 501 and visited[ny][nx] is False and graph[ny][nx] != float("inf"):
            visited[ny][nx] = True
            if graph[ny][nx] == 0:
                q.appendleft([cost, ny, nx])
            else:
                q.append([cost+1, ny, nx])

if not visited[500][500]:
    print(-1)

