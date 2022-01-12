import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

M, N = map(int, input().split())
graph = [list(f"{input()}") for _ in range(M)]

q = deque()
distances = [[float("inf")] * N for _ in range(M)]
distances[0][0] = 0

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]  #대각선

while q:
    cost, y, x = q.popleft()
    if cost > distances[y][x]:
        continue #하나가 더 있으면 통과

    else:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < M and 0 <= nx < N: # 8가지 경우의 수 탐색
                # 오른쪽 밑(y+1, x+1)으로 가는 것은 (y, x) 가 결정하고
                # 오른쪽 위(y-1, x+1)로 가는것은 (y-1, x) 가 결정하고
                # 왼쪽 위(y-1, x-1)로 가는것은 (y-1, x-1) 가 결정하고
                # 왼쪽 밑(y-1, x+1)으로 가는것은 (y, x-1) 가 결정한다 힝 골떄리네. 45도 돌려봐?
                if 0 <= y+1 < M and 0 <= x+1 < N












    print()

print()
for i in range(M):
    for j in range(N):
        print(distances[i][j], end = " ")
    print()


