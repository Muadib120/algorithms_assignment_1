import matplotlib.pyplot as plt
import numpy as np

# Data
dimensions = ['10,10', '5,20', '4,25', '2,50', '1,100', '20,5', '25,4', '50,2', '100,1']
array_times = [0.0026, 0.0023, 0.0024, 0.0027, 0.0028, 0.0025, 0.0029, 0.0026, 0.0026]
adjlist_times = [0.0035, 0.0032, 0.0034, 0.0038, 0.0037, 0.0034, 0.0035, 0.0047, 0.0043]
adjmat_times = [0.0249, 0.0262, 0.0295, 0.0372, 0.0438, 0.0273, 0.0285, 0.0377, 0.0479]

# Plot
bar_width = 0.25
x = np.arange(len(dimensions))
plt.figure(figsize=(12, 8))
plt.bar(x - bar_width, array_times, width=bar_width, label='2D Array', color='b')
plt.bar(x, adjlist_times, width=bar_width, label='Adjacency List', color='g')
plt.bar(x + bar_width, adjmat_times, width=bar_width, label='Adjacency Matrix', color='r')

# Labels and title
plt.xlabel('Dimensions (Row,Col)')
plt.ylabel('Average Time (seconds)')
plt.title('Time Efficiency for 100 Cell Mazes')
plt.xticks(x, dimensions)
plt.grid(axis='y', linestyle='--')

# Legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()