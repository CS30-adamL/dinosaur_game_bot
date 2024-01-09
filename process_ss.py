from PIL import ImageGrab, Image



# Construct the full path to the screenshot
def crop_screenshot(top_left,bottom_right):
    screenshot_path = "F:/GitHub/dinosaur_game_bot/screen_shots/screenshot.png"
    try:
        screenshot = Image.open(screenshot_path)
        crop_coords = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
        cropped_image = screenshot.crop(crop_coords)
        os.remove(screenshot_path)
        cropped_image.save("F:/GitHub/dinosaur_game_bot/screen_shots/cropped_screenshot.png")
    except FileNotFoundError:
        print(f"Screenshot not found")
