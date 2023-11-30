import matplotlib.pyplot as plt
import numpy as np

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([3, 7, 2, 8, 5])

# plt.scatter(x, y)
# plt.show()

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 7, 2, 8, 5])

plt.title('Scatter Plot')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.scatter(x, y, marker='|', color='red')
plt.show()