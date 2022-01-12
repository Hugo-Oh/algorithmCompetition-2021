import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

# __init__

def bfs(s_y, s_x):
    for i in range(M):  # s -> e 로 가는 경로 지정하기
        for j in range(N):
            if graph[i][j] == "/":
                paths[i][j].append([1, i + 1, j + 1])
                paths[i + 1][j + 1].append([1, i, j])
                 paths[i + 1][j].append([0, i, j + 1])
                paths[i][j + 1].append([0, i + 1, j])
ㄹㅁㅁsd
            else:
                paths[i][j].append([0, i + 1, j + 1])
                paths[i + 1][j + 1].append([0, i, j])
                paths[i + 1][j].append([1, i, j + 1])
                paths[i][j + 1].append([1, i + 1, j])

    q.appendleft(*paths[s_y][s_y])
    distances = [[float("inf")] * (N + 1) for _ in range(M + 1)]
    distances[s_y][s_x] = 0

    while q:
        cost, y, x = q.popleft()
        if cost > distances[y][x]:
            continue

        if y == M and x == N: #마지막 지점 발견한 경우
            answer = cost
            return answer

        for w, ny, nx in paths[y][x]:
            distance = cost + w
            if 0 <= ny < M+1 and 0 <= nx < N+1 and distance < distances[ny][nx]:
                distances[ny][nx] = distance
                if w == 1:
                    q.append([distance, ny, nx])
                else:
                    q.appendleft([distance, ny, nx])


M, N = map(int, input().split())
graph = [list(f"{input()}") for _ in range(M)]
paths = [[[] for _ in range(N + 1)] for _ in range(M + 1)]
visited = [[False] * (N + 1) for _ in range(M + 1)]
q = deque()

if (M + N) % 2 == 0:
    answer = bfs(0, 0)
    print(answer)
else:
    print("NO SOLUTION")
