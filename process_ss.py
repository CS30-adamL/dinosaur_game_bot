import cv2
import numpy as np
from PIL import Image

def preprocess_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a binary threshold to separate the foreground (dinosaur, obstacles) from the background
    _, binary_threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Extract information about the dinosaur and obstacles
    dinosaur_position = None
    obstacles_positions = []

    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)
        
        # Set a threshold to filter out small contours (noise)
        if area > 100:
            # Get the bounding box of the contour
            x, y, w, h = cv2.boundingRect(contour)
            
            # Check if it's the dinosaur (you might need to adjust this based on your game)
            if w > 30 and h > 30:
                dinosaur_position = (x, y, x + w, y + h)
            else:
                obstacles_positions.append((x, y, x + w, y + h))

    return dinosaur_position, obstacles_positions

# # Example usage:
# # Assuming you have captured a screenshot as 'screenshot.png'
# screenshot_path = 'path/to/save/screenshots/screenshot_1.png'
# screenshot = cv2.imread(screenshot_path)

# # Preprocess the image
# dinosaur_position, obstacles_positions = preprocess_image(screenshot)

# # Print the results
# print("Dinosaur Position:", dinosaur_position)
# print("Obstacles Positions:", obstacles_positions)
