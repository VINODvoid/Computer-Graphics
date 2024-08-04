import cv2
import numpy as np

# Load the image
image = cv2.imread('./human.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Edge Detection using Canny
edges = cv2.Canny(gray_image, 100, 200)

# Texture extraction using Laplacian
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)  # Convert back to 8-bit image

# Texture extraction using Sobel
sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
sobelx = cv2.convertScaleAbs(sobelx)  # Convert back to 8-bit image
sobely = cv2.convertScaleAbs(sobely)  # Convert back to 8-bit image
sobel_combined = cv2.bitwise_or(sobelx, sobely)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Edges (Canny)', edges)
cv2.imshow('Textures (Laplacian)', laplacian)
cv2.imshow('Textures (Sobel Combined)', sobel_combined)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
