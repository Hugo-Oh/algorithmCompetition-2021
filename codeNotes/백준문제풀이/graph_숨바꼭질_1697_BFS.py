import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())

time = [0] * 100001

queue = deque()
queue.append(N)

while queue:
    cur = queue.popleft()
    if cur == K:
        print(time[K])
        break
    if cur - 1 >= 0 and time[cur-1] == 0:
        time[cur-1] = time[cur] + 1
        queue.append(cur-1)
    if cur + 1 < 100001 and time[cur+1] == 0 :
        time[cur+1] = time[cur] + 1
        queue.append(cur+1)
    if cur * 2 < 100001 and time[2 * cur] == 0 :
        time[cur * 2] = time[cur] + 1
        queue.append(2*cur)
