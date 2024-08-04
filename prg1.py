import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
            
    return points

x1, y1, x2, y2 = 10, 10, 50, 30
line_points = bresenham_line(x1, y1, x2, y2)

x, y = zip(*line_points)
plt.plot(x, y, marker='o')
plt.title('Bresenham Line Drawing')
plt.show()
