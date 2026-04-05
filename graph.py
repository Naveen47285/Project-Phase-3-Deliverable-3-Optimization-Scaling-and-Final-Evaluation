import matplotlib.pyplot as plt

# Replace with YOUR actual values from output
sizes = [100, 1000, 5000, 10000]
times = [0.0008, 0.0010, 0.0046, 0.0060]

plt.plot(sizes, times, marker='o')
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Heap Performance Scaling")
plt.grid(True)

plt.show()