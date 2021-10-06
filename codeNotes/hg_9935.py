import sys
sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

word = input()
pattern = input()


while (pattern in word):
    start = word.index(pattern)
    end = start + len(pattern)
    word = word[:start] + word[end:]

print(word if word else "FRULA")


import sys
sys.stdin = open("input.txt", "rt")

stack = []
string = input()
bomb = list(input())

while string:
    check = False
    for s in string:
        stack.append(s)
        if stack[-len(bomb):] == bomb:
            check = True
            for _ in range(len(bomb)):
                stack.pop()

    string = "".join(stack)
    stack = []

    if not check:
        break

print(string if string else "FRULA")