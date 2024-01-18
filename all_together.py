from find_screen import findscreen
from get_screen import Capture_and_crop_screenshot
from process_ss import Process, test_pixels_in_Box
# from matching import find_image
import pyautogui
import time 
D_top_left = (27,67)
D_bottom_right =(67,110)
top_left_corner, bottom_right_corner, dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright = findscreen()
# def intailize():
#     dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img,cropped_image = Capture_and_crop_screenshot(top_left_corner, bottom_right_corner, dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright)
#     D_top_left,D_bottom_right,D_bottom_left,D_top_right, D_lowest_y = find_image("GitHub\dinosaur_game_bot\Dino2.png","GitHub\dinosaur_game_bot\screen_shots\cropped_screenshot.png")
#     pyautogui.press('space')
#     time.sleep(.3)
#     dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img,cropped_image = Capture_and_crop_screenshot(top_left_corner, bottom_right_corner, dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright)
#     DG_top_left,DG_bottom_right,DG_bottom_left,DG_top_right, DG_lowest_y = find_image("GitHub\dinosaur_game_bot\Dino2.png","GitHub\dinosaur_game_bot\screen_shots\cropped_screenshot.png")
#     print(f"{D_top_left,D_bottom_right,D_bottom_left,D_top_right, D_lowest_y} || {DG_top_left,DG_bottom_right,DG_bottom_left,DG_top_right, DG_lowest_y}")
def game_image():
    dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img,cropped_image = Capture_and_crop_screenshot(top_left_corner, bottom_right_corner, dinosaur_viewbox_Topleft,dinosaur_viewbox_bottomright)
    if Process(dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img,cropped_image):
        pyautogui.press('space')
        # time.sleep(0.2)
        # if test_pixels_in_Box(D_top_left[0], D_top_left[1] ,D_bottom_right[0],D_bottom_right[1] ,cropped_image):
        #     print("down arrow")
        #     pyautogui.press('down',presses=1, interval=0.8,)
        # else:
        #     pass

# intailize()
for x in range(10000):
    game_image()                              