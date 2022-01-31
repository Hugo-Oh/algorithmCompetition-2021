import sys
sys.stdin = open("input.txt", "rt")

S = input()
stack = []
num_li = []

num = 0
for s in S:
    if s == "(" or s == "[":
        stack.append(s)

    elif s == "]" and stack[-1] == "[":
        stack.pop()
        num_li.append(3)

    elif s == ")" and stack[-1] == "(":
        stack.pop()
        num_li.append(2)


print(num_li)

print(stack)

