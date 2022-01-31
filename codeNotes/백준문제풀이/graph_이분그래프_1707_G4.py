import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

T = int(input())


def bfs(start):
    q = deque()
    q.append(start)

    if visited[start] == 0:
        visited[start] = 1

    while q:
        v = q.popleft()
        color = visited[v]
        for vv in graph[v]:
            if visited[vv] == 0:
                if color == 1:
                    visited[vv] = 2
                else:
                    visited[vv] = 1
                q.append(vv)

            else:
                if visited[vv] == color: # 1, 1 이 겹치거나 2,2가 겹치는 모순 발생시
                    return False
    return True

for _ in range(T):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    graph = [[] for _ in range(V+1)]
    checker = True

    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1, V+1):
        if not bfs(i):
            checker = False

    print("YES" if checker else "NO")


