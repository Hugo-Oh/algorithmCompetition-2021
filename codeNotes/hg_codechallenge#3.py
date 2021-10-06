import sys
input = sys.stdin.readline

numbers = [1,2,3,4,6,7,8,0]
std = sum(list(range(1, 10)))
minn = sum(numbers)



answer = std - minn
print(answer)

