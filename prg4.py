import matplotlib.pyplot as plt
import numpy as np

def transform_2d(points, matrix):
    return np.dot(points, matrix)

square = np.array([[0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 1]])

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

ax.plot(square[:, 0], square[:, 1], label='Original')

# Translation matrix
trans_matrix = np.array([[1, 0, 2],
                         [0, 1, 3],
                         [0, 0, 1]])
translated_square = transform_2d(square, trans_matrix)
ax.plot(translated_square[:, 0], translated_square[:, 1], label='Translated')

# Scaling matrix
scale_matrix = np.array([[2, 0, 0],
                         [0, 2, 0],
                         [0, 0, 1]])
scaled_square = transform_2d(square, scale_matrix)
ax.plot(scaled_square[:, 0], scaled_square[:, 1], label='Scaled')

plt.title('2D Transformations')
plt.legend()
plt.show()
