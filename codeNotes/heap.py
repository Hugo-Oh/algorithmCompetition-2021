
def max_heap_insert(heap, key):
    heap_size = len(heap)
    heap.append(key)
    i = heap_size
    while (i > 1 and heap[PARENT(i)] < A[i]):
