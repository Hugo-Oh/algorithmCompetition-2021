import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
array = list(map(int, input().split()))
array.insert(0, 0)
dp = array.copy()

tot = 0
for now in range(1, N+1):
    for before in range(now):
        if array[now] > array[before]:
            dp[now] = max(dp[now], dp[before] + array[now])




print(dp)
