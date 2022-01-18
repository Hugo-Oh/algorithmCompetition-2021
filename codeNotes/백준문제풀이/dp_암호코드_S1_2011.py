import sys
sys.stdin = open("input.txt", "rt")

num = "0" + input()
if num[1] == "0":
    print(0)
else:
    n = len(num)
    dp = [0] * (n)

    for now in range(n):
        if now == 0:
            dp[0] = 1

        if 10 <= int(num[now - 1] + num[now]) <= 26:
            dp[now] += dp[now - 2]
        dp[now] += dp[now - 1]
    print(dp[n-1])
    print(dp)
