import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1,8, 10])
# ypoints = np.array([3, 10, 5])

# plt.figure(figsize=(5,5))
# plt.plot(xpoints, ypoints, color='red')
# plt.xlim([0,15])
# plt.ylim([0,15])
# plt.show()

xpoints = np.array([1,8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(10,5))
plt.plot(xpoints, ypoints, color='blue',marker='o', linestyle='-.', linewidth=3)
plt.xlabel('Sumbu X', fontsize=14)
plt.ylabel('Sumbu Y', fontsize=14)
plt.xlim([0,15])
plt.ylim([0,15])
plt.show()