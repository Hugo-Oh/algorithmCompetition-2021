import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

M, N = map(int, input().split())
graph = [list(f"{input()}") for _ in range(M)]

q = deque()
paths = [[[] for _ in range(N+1)] for _ in range(M+1)]
visited = [[[False] for _ in range(N+1)] for _ in range(M+1)]

for i in range(M): # s -> e 로 가는 경로 지정하기
    for j in range(N):
        if graph[i][j] == "/":
            paths[i][j].append([1, i+1, j+1])
            paths[i+1][j+1].append([1, i, j])
            paths[i+1][j].append([0, i, j+1])
            paths[i][j+1].append([0, i+1, j])

        else:
            paths[i][j].append([0, i+1, j+1])
            paths[i+1][j+1].append([0, i, j])
            paths[i+1][j].append([1, i, j+1])
            paths[i][j+1].append([1, i+1, j])

# __init__
q.appendleft(*paths[0][0])
visited[0][0] = True
distances = [[float("inf")] * (N+1) for _ in range(M+1)]
distances[0][0] = 0


while q:
    cost, y, x = q.popleft()
    if cost > distances[y][x]:
        continue
    if y == M and x == N:
        answer = cost
        break
    for w, ny, nx in paths[y][x]:
        distance = cost + w
        if 0 <= ny < M+1 and 0 <= nx < N+1 and distances[ny][nx] > distance:
            distances[ny][nx] = distance
            if w == 1:
                q.append([distance, ny, nx])
            else:
                q.appendleft([distance, ny, nx])

if (M + N) % 2 == 0:
    print(answer)
else:
    print("NO SOLUTION")