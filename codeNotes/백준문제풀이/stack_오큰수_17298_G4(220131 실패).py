import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")

N = int(input())

arr = list(map(int, input().split()))

heap = [(index, -value) for index, value in enumerate(arr)]
hq.heapify(heap)

print(heap)

#value은 크면서 index는 최소값을 넣자 - > index heapq, -value heapq
# 우선순위는 당연히 value 큰것들 중, 그 다음에 index 최소값 즉 (-value, heapq)가 된다.




