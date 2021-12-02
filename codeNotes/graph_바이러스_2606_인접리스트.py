import sys
sys.stdin = open("input.txt", "rt")

# 인접리스트로 풀기
N = int(input())
V = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
visited = []
counter = 0

for _ in range(V):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

start = 1
def dfs(nowNode):
    global counter
    visited.append(nowNode)
    for nextNode in graph[nowNode]:
        if nextNode not in visited:
            counter += 1
            dfs(nextNode)

dfs(start)
print(counter)
