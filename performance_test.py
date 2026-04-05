import time
import random
from heap_optimized import MinHeap

# Generate random dataset
def generate_data(n):
    return [random.randint(1, 100000) for _ in range(n)]

# -----------------------------
# Performance Testing (Scaling)
# -----------------------------
print("Performance Testing:\n")

sizes = [100, 1000, 5000, 10000]

for size in sizes:
    data = generate_data(size)
    heap = MinHeap()

    start = time.time()

    for val in data:
        heap.insert(val)

    end = time.time()

    print(f"Size: {size}, Time: {end-start:.4f}s, Operations: {heap.operations}")

# -----------------------------
# Stress Testing
# -----------------------------
print("\nRunning stress test...")

data = generate_data(20000)
heap = MinHeap()

start = time.time()

for val in data:
    heap.insert(val)

while heap.heap:
    heap.extract_min()

end = time.time()

print(f"Stress test completed successfully in {end-start:.4f}s")