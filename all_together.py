from find_screen import findscreen
from process_ss import Capture_and_crop_screenshot
import pyautogui
import time 

top_left_corner, bottom_right_corner, dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright = findscreen()

def game_image():
    if Capture_and_crop_screenshot(top_left_corner, bottom_right_corner, dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright):
        pyautogui.press('space')
        # time.sleep(0.05)

for x in range(10000):
    game_image()                            