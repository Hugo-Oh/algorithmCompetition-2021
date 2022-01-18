import sys

s = "one4seveneight"

decode = {"zero" : 0, "one" : 1, "two" : 2,"three" : 3,"four" : 4,"five" : 5,"six" : 6 ,"seven" : 7,"eight" : 8,"nine" : 9}

character = ""
answer = []
for c in s:
    if c.isdigit():
        print(c)
        answer.append(int(c))
        continue

    character += c
    if character in decode:

        answer.append(decode[character])
        character = ""

answer = "".join(map(str, answer))

