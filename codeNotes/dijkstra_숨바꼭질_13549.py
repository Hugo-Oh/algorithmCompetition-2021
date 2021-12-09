import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

n, k = map(int, input().split())
dp = [inf] * (100001)
heap = []


def dijkstra(n, k):
    if k <= n:
        print(n - k)
        return

    heappush(heap, [0, n])
    while heap:
        w, n = heappop(heap)
        for nx in [n + 1, n - 1, n * 2]:
            if 0 <= nx <= 100000:
                if nx == n * 2 and dp[nx] == inf:
                    dp[nx] = w
                    heappush(heap, [w, nx])
                elif dp[nx] == inf:
                    dp[nx] = w + 1
                    heappush(heap, [w + 1, nx])
    print(dp[k])


dijkstra(n, k)