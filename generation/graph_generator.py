import matplotlib.pyplot as plt

# Data for array type
array_dimensions = [1, 5, 10, 20, 30, 40, 50, 75, 100]
array_times = [0.0001, 0.0024, 0.0085, 0.0308, 0.0634, 0.1084, 0.1734, 0.3840, 0.2067]

# Data for adjlist type
adjlist_dimensions = [1, 5, 10, 20, 30, 40, 50, 75, 100]
adjlist_times = [0.0002, 0.0036, 0.0131, 0.0461, 0.0975, 0.1792, 0.2768, 0.6323, 0.3562]

# Data for adjmat type
adjmat_dimensions = [1, 5, 10, 20, 30, 40, 50, 75, 100]
adjmat_times = [0.0002, 0.0061, 0.0418, 0.4243, 1.9009, 5.7121, 13.3583, 51.9724, 198.8947]

# Plotting
plt.figure(figsize=(10, 6))



plt.plot(array_dimensions, array_times, marker='o', label='2D Array')
plt.plot(adjlist_dimensions, adjlist_times, marker='o', label='Adjacency List')
plt.plot(adjmat_dimensions, adjmat_times, marker='o', label='Adjacency Matrix')

plt.title('Time efficency of a square maze for multiple data types')
plt.xlabel('Dimensions of square maze')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()