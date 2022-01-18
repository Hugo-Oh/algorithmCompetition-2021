import sys
sys.stdin = open("input.txt", "rt")

# 인접행렬로 풀기
N = int(input())
V = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
counter = 0
for _ in range(V):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

def DFS(Node):
    global counter
    visited[Node] = 1

    for nextNode in range(1, N+1):
        if graph[Node][nextNode] == 1 and visited[nextNode] == 0:
            DFS(nextNode)
            counter += 1

DFS(1)
print(counter)
