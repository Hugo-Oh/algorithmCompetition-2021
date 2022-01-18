import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
s_y, s_x, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


cnt =- 0
def clearRoom(y, x, d):
    global cnt
    visited[y][x] = True
    cnt += 1
    if d == 0 and 0 <= y < N and 0 <= x-1 < M and visited[y][x-1] is False:
        clearRoom(y, x-1, 3)

    elif d == 1 and 0 <= y-1 < N and 0 <= x < M and visited[y-1][x] is False:
        clearRoom(y-1, x, 0)

    elif d == 2 and 0 <= y < N and 0 <= x+1 < M and visited[y][x+1] is False:
        clearRoom(y, x+1, 1)

    elif d == 3 and 0 <= y+1 < N and 0 <= x < M and visited[y+1][x] is False:
        clearRoom(y+1, x, 2)


clearRoom(s_y, s_x, d)

print(cnt)




