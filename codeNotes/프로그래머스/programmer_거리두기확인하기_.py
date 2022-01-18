import sys
from collections import deque

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]



def bfs(place, y, x):
    visited = [[False] * 5 for _ in range(5)]
    graph = [[float("inf")] * 5 for _ in range(5)]
    people = []
    q = deque()
    dx= [-1, 0, 1, 0]
    dy= [0, -1, 0, 1]

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                people.append([0, i, j])

    q.append(people[0])
    visited[0][0] = True

    while q:
        cost, y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] is False:
                if place[ny][nx] != "X":
                    visited[ny][nx] = True
                    graph[ny][nx] = cost + 1
                    q.append([cost+1, ny, nx])

    for _, y, x in people:
        print(graph[y][x])


    for c in graph:
        print(c)

bfs(places[0], 0, 0)