import time
# import pyautogui
from PIL import ImageGrab

# Path to save the screenshots
def Capture_screenshot():
    save_path = "F:/GitHub/dinosaur_game_bot/screen_shots/"
    screenshot = ImageGrab.grab()
    screenshot.save(f"{save_path}screenshot.png")
    print("Screenshots captured successfully.")

