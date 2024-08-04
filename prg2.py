import matplotlib.pyplot as plt

def draw_square(ax, vertices, color='blue'):
    square = plt.Polygon(vertices, closed=True, fill=None, edgecolor=color)
    ax.add_patch(square)

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

square = [(0, 0), (2, 0), (2, 2), (0, 2)]

draw_square(ax, square)

# Translation
translated_square = [(x + 2, y + 3) for x, y in square]
draw_square(ax, translated_square, color='red')

# Scaling
scaled_square = [(x * 2, y * 2) for x, y in square]
draw_square(ax, scaled_square, color='green')

plt.title('2D Geometric Operations')
plt.show()
