class MinHeap:
    def __init__(self):
        self.heap = []
        self.operations = 0  # Track operations for performance analysis

    # Insert element into heap
    def insert(self, value):
        self.operations += 1
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # Extract minimum element
    def extract_min(self):
        self.operations += 1
        if not self.heap:
            return None

        # Swap root with last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        min_val = self.heap.pop()

        # Restore heap property
        self._heapify_down(0)

        return min_val

    # 🔥 Optimized iterative heapify up
    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                # Swap
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    # 🔥 Optimized iterative heapify down
    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                # Swap
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    # 🔥 Optimized bulk heap construction (O(n))
    def build_heap(self, arr):
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    # Optional: Display heap
    def display(self):
        return self.heap