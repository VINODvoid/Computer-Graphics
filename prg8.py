import cv2
import numpy as np

# Load the image
image = cv2.imread('./human.png')

# Get image dimensions
height, width = image.shape[:2]

# 1. Translation
# Define the translation matrix (shift right by 100 pixels and down by 50 pixels)
tx, ty = 100, 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

# 2. Scaling
# Scale the image by a factor of 1.5
scale_x, scale_y = 1.5, 1.5
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

# 3. Rotation
# Define the rotation matrix (rotate by 45 degrees around the center of the image)
angle = 45
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Rotated Image', rotated_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
