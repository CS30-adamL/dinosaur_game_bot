# import time
# import subprocess
import os
import subprocess
# # Path to save the screenshots
# save_path = "/Users/Adam/Documents/GitHub/dinosaur_game_bot/screen_shots/"
# input_folder = '/Users/Adam/Documents/GitHub/dinosaur_game_bot/screen_shots'
# output_folder = '/Users/Adam/Documents/GitHub/dinosaur_game_bot/processed_images/'
# # Ensure the game is in focus before running the script
# print("Switch to the Chrome Dinosaur Game window...")


def Capture_screenshot():
    # Use subprocess to call the 'screencapture' command on macOS
    screenshot_path = os.path.join(save_path, f"screenshot_.png")
    subprocess.run(["screencapture", screenshot_path])
    print("Screenshot captured successfully.")
    return screenshot_path


# Path to save the screenshots
save_path = "/Users/Adam/Documents/GitHub/dinosaur_game_bot/screen_shots/"
input_folder = '/Users/Adam/Documents/GitHub/dinosaur_game_bot/screen_shots'
output_folder = '/Users/Adam/Documents/GitHub/dinosaur_game_bot/processed_images/'

# Ensure the game is in focus before running the script
print("Switch to the Chrome Dinosaur Game window...")
# def Capture_screenshot():
#     # Use subprocess to call the 'screencapture' command on macOS
#     screenshot_path = os.path.join(save_path, f"screenshot_.png")
    
#     print("Screenshot captured successfully.")
#     return screenshot_path

