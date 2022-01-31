import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

S = input()
stack = []
num = ""
num_li = []
ks = []
answer = 0


for s in S:
    if s.isdigit():
        stack.append(s)

    elif s == "(":
        last = stack.pop()
        while stack:
            temp = stack.pop()
            num += temp

        num_li.append(num[::-1])
        num = ""
        ks.append(int(last))

    elif s == ")":
        while stack:
            temp = stack.pop()
            num += temp

        num_li.append(num[::-1])
        num = ""

print(num_li)
print(ks)
for k in ks[::-1]:
    temp = num_li.pop()
    if temp == "":
        continue
    else:
        print(len(temp * k))
        answer += len(temp) * k

print(len(num_li))
answer += len(num_li[0])

print(ks)
print(num_li)
print(answer)





