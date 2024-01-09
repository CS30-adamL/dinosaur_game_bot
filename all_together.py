from find_screen import get_game_coordinates
from get_screen import Capture_screenshot
from process_ss import crop_screenshot
print("starting bot")

top_left_corner, bottom_right_corner, dinosaur_position = get_game_coordinates()
Capture_screenshot()
crop_screenshot(top_left_corner,bottom_right_corner)
