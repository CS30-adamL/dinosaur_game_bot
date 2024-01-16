import cv2
import numpy as np

def find_image(template_path,screenshot_path):
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
    threshold = 0.75

    if max_val >= threshold:

        # Get the dimensions of the template
        h, w = template_gray.shape

        # Extract the coordinates of the matched region
        top_left = max_loc
        top_right = (top_left[0] + w,top_left[1])
        bottom_right = (top_left[0] + w, top_left[1] + h)
        bottom_left = (top_left[0], top_left[1] + h)

        # Print the lowest y-coordinate, bottom-left, and bottom-right corners
        lowest_y = bottom_right[1]  # Assuming y-coordinates increase downwards
        print("Lowest y-coordinate:", lowest_y)
        print("Top-left corner:", top_left)
        print("Bottom-right corner:", bottom_right)
        print("Bottom-left corner:", bottom_left)
        # Draw a rectangle around the matched region
        h, w = template_gray.shape
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
        # Display the result
        cv2.imshow('Matched Image', screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return top_left,bottom_right,bottom_left,top_right, lowest_y
#         # Display the result
#         cv2.imshow('Matched Image', screenshot)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     else:
#         print("Image not found in the screenshot.")

# # Example usage
find_image('F:\GitHub\dinosaur_game_bot\Dino2.png', 'F:\GitHub\dinosaur_game_bot\screen_shots\cropped_screenshot.png')