import time
import pyautogui
from PIL import ImageGrab
import process_ss
# Set the interval between each screenshot in seconds
interval = .2

# Number of screenshots to capture
num_screenshots = 10

# Path to save the screenshots
save_path = "F:/GitHub/dinosaur_game_bot/screen_shots/"

# Ensure the game is in focus before running the script
print("Switch to the Chrome Dinosaur Game window...")
time.sleep(5)  # Wait for 5 seconds to switch focus

# Capture screenshots
for i in range(num_screenshots):
    # Capture screenshot using pyautogui
    screenshot = ImageGrab.grab()
    process_ss.preprocess_image(screenshot)
    # Save the screenshot
    screenshot.save(f"{save_path}screenshot_{i+1}.png")
    
    # Wait for the specified interval before capturing the next screenshot
    time.sleep(interval)

print("Screenshots captured successfully.")

