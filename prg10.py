import cv2

# Load the image
image = cv2.imread('./human.png')

# Apply Averaging
average_blur = cv2.blur(image, (5, 5))

# Apply Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Median Blur
median_blur = cv2.medianBlur(image, 5)

# Apply Bilateral Filter
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Averaging', average_blur)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Filter', bilateral_blur)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
