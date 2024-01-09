import pyautogui
import time

def get_mouse_click_coordinates():
    print("Click on the top-left corner of the game window.")
    time.sleep(2)
    top_left = pyautogui.position()
    print("Top-left coordinates:", top_left)

    time.sleep(2)  # Pause for 2 seconds before the next click

    print("Click on the bottom-right corner of the game window.")
    bottom_right = pyautogui.position()
    print("Bottom-right coordinates:", bottom_right)

    time.sleep(2)  # Pause for 2 seconds before the next click

    print("Click on the position of the dinosaur.")
    dinosaur_position = pyautogui.position()
    print("Dinosaur position coordinates:", dinosaur_position)

    return top_left, bottom_right, dinosaur_position

# Example usage:
top_left, bottom_right, dinosaur_position = get_mouse_click_coordinates()

# Log the coordinates or use them as needed in your script
print("Top-left coordinates:", top_left)
print("Bottom-right coordinates:", bottom_right)
print("Dinosaur position coordinates:", dinosaur_position)
