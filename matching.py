import cv2
import numpy as np

def find_image("GitHub\dinosaur_game_bot\Dino.png", cropped_screenshot):
    # Read the template image and the screenshot
    template = cv2.imread(template_path)
    screenshot = cv2.imread(screenshot_path)

    # Convert images to grayscale
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Find the template in the screenshot using template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Define a threshold for matching
    threshold = 0.8

    if max_val >= threshold:
        # Draw a rectangle around the matched region
        h, w = template_gray.shape
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)

        # Display the result
        cv2.imshow('Matched Image', screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image not found in the screenshot.")

# Example usage
find_image('template.png', 'screenshot.png')