import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_cube(ax, vertices, color='blue'):
    faces = [[vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]], 
             [vertices[j] for j in [0, 1, 5, 4]], 
             [vertices[j] for j in [2, 3, 7, 6]], 
             [vertices[j] for j in [0, 3, 7, 4]], 
             [vertices[j] for j in [1, 2, 6, 5]]]
    poly3d = Poly3DCollection(faces, alpha=.25, linewidths=1, edgecolors=color)
    poly3d.set_facecolor(color)
    ax.add_collection3d(poly3d)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-2, 4])
ax.set_ylim([-2, 4])
ax.set_zlim([-2, 4])

cube = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                 [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

draw_cube(ax, cube)

# Translation
translated_cube = cube + np.array([1, 1, 1])
draw_cube(ax, translated_cube, color='red')

# Scaling
scaled_cube = cube * 2
draw_cube(ax, scaled_cube, color='green')

plt.title('3D Geometric Operations')
plt.show()
