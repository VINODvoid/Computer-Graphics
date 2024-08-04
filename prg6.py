import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animation Effects")

# Colors
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Create objects
objects = [
    {
        "x": random.randint(50, WIDTH - 50),
        "y": random.randint(50, HEIGHT - 50),
        "radius": random.randint(10, 20),
        "speedx": random.randint(-5, 5),
        "speedy": random.randint(-5, 5),
        "color": random.choice(COLORS),
    }
    for _ in range(10)
]

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    for obj in objects:
        # Update object position
        obj["x"] += obj["speedx"]
        obj["y"] += obj["speedy"]

        # Check for collision with screen boundaries
        if obj["x"] - obj["radius"] < 0 or obj["x"] + obj["radius"] > WIDTH:
            obj["speedx"] = -obj["speedx"]
        if obj["y"] - obj["radius"] < 0 or obj["y"] + obj["radius"] > HEIGHT:
            obj["speedy"] = -obj["speedy"]

        # Draw the object
        pygame.draw.circle(screen, obj["color"], (obj["x"], obj["y"]), obj["radius"])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
