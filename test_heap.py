from heap import MinHeap

heap = MinHeap()

heap.insert(10)
heap.insert(5)
heap.insert(20)

assert heap.extract_min() == 5
assert heap.extract_min() == 10
assert heap.extract_min() == 20
assert heap.extract_min() is None

print("All test cases passed!")