from find_screen import findscreen
from process_ss import Capture_and_crop_screenshot
import pyautogui
import time 

top_left_corner, bottom_right_corner, dinosaur_position = findscreen()

def game_image():
    if Capture_and_crop_screenshot(top_left_corner, bottom_right_corner,dinosaur_position):
        pyautogui.press('space')
        time.sleep(0.1)

for x in range(1000):
    game_image()