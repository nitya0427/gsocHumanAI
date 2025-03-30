import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the processed image
processed_image_path = "gsoc/processed_spanish.jpg"
img = cv2.imread(processed_image_path)

# Convert to grayscale (if not already)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Run OCR with Spanish language support
custom_config = r'--oem 1 --psm 6 -l spa'  # Spanish language model, PSM 6 for blocks of text
extracted_text = pytesseract.image_to_string(gray, config=custom_config)

# Save the extracted text to a file
text_output_path = "gsoc/extracted.txt"
with open(text_output_path, "w", encoding="utf-8") as f:
    f.write(extracted_text)

# Print the extracted text
print("Extracted Text:\n", extracted_text)
