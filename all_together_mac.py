import find_game_mac
import get_screen_mac
# import process_image_mac
#find the game




top_left, bottom_right, dinosaur_position = find_game_mac.get_mouse_click_coordinates()
screen_shot = get_screen_mac.Capture_screenshot()

screen_shot.save("/Users/Adam/Documents/GitHub/dinosaur_game_bot/screen_shots/screenshot_.png")
# cropped_ss = process_image_mac.crop_and_process_image(screen_shot, top_left, bottom_right)
# cropped_ss.save(f"/Users/Adam/Documents/GitHub/dinosaur_game_bot/processed_images/screenshot_.png")
