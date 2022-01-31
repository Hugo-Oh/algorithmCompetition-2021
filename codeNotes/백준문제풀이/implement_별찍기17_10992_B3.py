import sys
sys.stdin = open("input.txt", "rt")

N = int(input())


for i in range(N):
    for j in range(2*i + 1):
        if i == N - 1:
            print("*", end = "")

        elif i == 0:



