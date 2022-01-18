import sys
sys.stdin = open("input.txt", "rt")
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

ny = [1, -1, 0, 0]
nx = [0, 0, -1, 1]
address = 2 # 1부터하면 중복카운팅이므로
count = 0

def DFS(y, x, start):
    global count
    graph[y][x] = start
    visited[y][x] = 1

    for dy, dx in zip(ny, nx):
        next_y, next_x = y + dy, x + dx
        if 0 <= next_y < N and 0 <= next_x < N:
            if graph[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                DFS(next_y, next_x, start)
    count += 1
count_li = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            DFS(y, x, address)
            address += 1
            count_li.append(count)
            count = 0
print(address - 2)
for cunter in sorted(count_li):
    print(cunter)