from heap import MinHeap

heap = MinHeap()

# Insert elements
heap.insert(10)
heap.insert(5)
heap.insert(20)

print("Heap after insert:", heap.heap)

# Extract min
print("Extracted:", heap.extract_min())
print("Heap after extract:", heap.heap)