import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
graphh = [list(map(int, input().split())) for _ in range(N)]

minn = min([min(x) for x in graphh])
maxx = max([max(x) for x in graphh])
# print(minn)
# print(maxx)
nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]
ans = 0

def sum_graph(graph, summ):
    for y in range(N):
        for x in range(N):
            graph[y][x] = graph[y][x] + summ

def dfs(y, x):
    copy[y][x] = -100 # 방문처리
    for dy, dx in zip(ny, nx):
        next_y, next_x = y + dy, x + dx
        if 0 <= next_y < N and 0 <= next_x < N and copy[next_y][next_x] > 0:
            dfs(next_y, next_x)


for standard in range(minn, maxx):  # maxx - 1 까지
    copy = [x[:] for x in graphh]
    sum_graph(copy, -standard)
    counter = 0

    for y in range(N):
        for x in range(N):
            if copy[y][x] > 0:
                dfs(y, x)
                counter += 1

    if counter > ans:
        ans = counter

print(ans if ans > 0 else 1)