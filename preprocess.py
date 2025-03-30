import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the processed image in grayscale
image_path = "gsoc/spanish.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 1: Apply Adaptive Thresholding to control black intensity
adaptive_thresh = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

# Step 2: Erode the text to make it thinner
kernel = np.ones((1,1), np.uint8)  # Adjust kernel size for thinning
thinned = cv2.erode(adaptive_thresh, kernel, iterations=1)

# Step 3: Sharpening the text for clarity
sharpen_kernel = np.array([[-1, -1, -1], 
                            [-1,  9, -1], 
                            [-1, -1, -1]])
sharpened = cv2.filter2D(thinned, -1, sharpen_kernel)

output_path = "gsoc/processed_spanish.jpg"
cv2.imwrite(output_path, sharpened)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Before")
plt.imshow(image, cmap='gray')
plt.subplot(1,2,2)
plt.title("After")
plt.imshow(sharpened, cmap='gray')
plt.tight_layout()
plt.show()


output_path