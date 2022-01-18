import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

array = [int(input()) for _ in range(N)]

def getMean(arr):
    answer = int(round(sum(arr) / len(arr), 0))

    return answer

def getMedian(arr):
    arr.sort()
    length = len(arr)import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

array = [int(input()) for _ in range(N)]

def getMean(arr):
    answer = int(round(sum(arr) / len(arr), 0))

    return answer

def getMedian(arr):
    arr.sort()
    length = len(arr)
    answer = arr[length//2]

    return answer

def getMode(arr):
    dic = {key: 0 for key in array}
    li = []

    for num in arr:
        dic[num] += 1

    maxx = max(dic.values())

    for key, value in dic.items():
        if value == maxx:
            li.append(key)
    li.sort()
    answer = li[0] if len(li) == 1 else li[1]

    return answer

def getRange(arr):
    maxx = max(arr)
    minn = min(arr)
    answer = maxx - minn
    return answer


print(getMean(array))
print(getMedian(array))
print(getMode(array))
print(getRange(array))

    answer = arr[length//2]

    return answer

def getMode(arr):
    dic = {key: 0 for key in array}
    li = []

    for num in arr:
        dic[num] += 1

    maxx = max(dic.values())

    for key, value in dic.items():
        if value == maxx:
            li.append(key)
    li.sort()
    answer = li[0] if len(li) == 1 else li[1]

    return answer

def getRange(arr):
    maxx = max(arr)
    minn = min(arr)
    answer = maxx - minn
    return answer


print(getMean(array))
print(getMedian(array))
print(getMode(array))
print(getRange(array))

