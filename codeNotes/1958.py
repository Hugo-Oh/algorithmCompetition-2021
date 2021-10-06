import sys
sys.stdin = open("input.txt", "rt")
"""
A = input()
B = input()
C = input()
arr = [[[0 for i in range(len(A)+1)] for j in range(len(B)+1)] for w in range(len(C)+1)]

for w in range(len(C)):
    for j in range(len(B)):
        for i in range(len(A)):
            if A[i] == B[j] == C[w]:
                # 3개가 같다면 (축기준 -1) + 1
                arr[w+1][j+1][i+1] = arr[w][j][i]+1
            else:
                # 3개중 하나라도 같지 않다면(즉, LCS에 하등 도움이 안되는 모든 경우) 각 축을 기준으로 한칸 떨어진 것 중 큰 값을 가져온다.
                arr[w+1][j+1][i+1] = max(arr[w][j+1][i+1],arr[w+1][j][i+1], arr[w+1][j+1][i])

print(arr[len(C)][len(B)][len(A)])"""

string = []
for i in range(3):
    string.append(input())

string = sorted(string,key=len)
for i in range(len(string[0]),0,-1):
    flag = False
    cnt = len(string[0])+1-i
    for j in range(cnt):
        chk = string[0][j:j+i]
        if chk in string[1] and chk in string[2]:
            print(i)
            flag = True
            break
    if flag:
        break