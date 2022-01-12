import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())


def bfs(N, K):
    q = deque()
    q.appendleft(N)
    graph = [0] * 100001
    visited = [False] * 100001
    visited[N] = True

    if K < N:
        print(N - K)
        return

    while q:
        now = q.popleft()


        if now == K:
            print(graph[K])
            return

        for n_step in (2*now, now-1, now+1):
            if 0 <= n_step < 100001 and visited[n_step] is False:
                visited[n_step] = True
                if n_step == 2 * now:
                    graph[n_step] = graph[now]
                    q.appendleft(n_step)
                else:
                    q.append(n_step)
                    graph[n_step] = graph[now] + 1

bfs(N, K)