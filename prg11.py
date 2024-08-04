import cv2

# Load the image
image = cv2.imread('./human.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve contour detection
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform edge detection using Canny
edges = cv2.Canny(blurred_image, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
contoured_image = image.copy()
cv2.drawContours(contoured_image, contours, -1, (0, 255, 0), 2)

# Display the original, edge, and contoured images
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.imshow('Contours', contoured_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
