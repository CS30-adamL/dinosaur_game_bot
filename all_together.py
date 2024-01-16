from find_screen import findscreen
from get_screen import Capture_and_crop_screenshot
from process_ss import Process
import pyautogui
import time 

top_left_corner, bottom_right_corner, dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright = findscreen()

def game_image():
    dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img,cropped_image = Capture_and_crop_screenshot(top_left_corner, bottom_right_corner, dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright)
    if Process(dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img,cropped_image):
        pyautogui.press('space')
        
        # time.sleep(0.05)

for x in range(10000):
    game_image()                            