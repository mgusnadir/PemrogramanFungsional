import matplotlib.pyplot as plt
import numpy as np

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1, label='Garis 1')
# plt.plot(y2, label='Garis 2')

# plt.title('Plot Dua Garis')
# plt.xlabel('Nilai X')
# plt.ylabel('Nilai Y')

# plt.legend()
# plt.show()

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([8, 3, 4, 9])
y4 = np.array([1, 2, 10, 12])

plt.plot(y1, label='Garis 1', color='blue', marker='*', linestyle='-.')
plt.plot(y2, label='Garis 2', color='green', marker='o', linestyle='--')
plt.plot(y3, label='Garis 3', color='red', marker='+', linestyle='-')
plt.plot(y4, label='Garis 4', color='purple', marker='|', linestyle=':')

plt.title('Plot Empat Garis')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.legend()
plt.show()