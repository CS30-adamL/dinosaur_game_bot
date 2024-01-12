from PIL import ImageGrab, Image


# # Path to save the screenshots
# def Capture_screenshot():
#     save_path = "F:/GitHub/dinosaur_game_bot/screen_shots/"
#     screenshot = ImageGrab.grab()
#     screenshot.save(f"{save_path}screenshot.png")
#     print("Screenshots captured successfully.")


# Construct the full path to the screenshot
def Capture_and_crop_screenshot(top_left,bottom_right,dinosaur):
    screenshot = ImageGrab.grab()
    crop_coords = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
    cropped_image = screenshot.crop(crop_coords)
    test_pixel = screenshot.getpixel(dinosaur)
    if calculate_luminance(test_pixel): 
        return True
    else:
        return False
    # cropped_image.save(f"F:/GitHub/dinosaur_game_bot/screen_shots/cropped_screenshot.png")



def calculate_luminance(color):
    # Calculate relative luminance for sRGB color
    r, g, b = color
    r = r / 255.0 if r <= 0.03928 else ((r / 255.0 + 0.055) / 1.055) ** 2.4
    g = g / 255.0 if g <= 0.03928 else ((g / 255.0 + 0.055) / 1.055) ** 2.4
    b = b / 255.0 if b <= 0.03928 else ((b / 255.0 + 0.055) / 1.055) ** 2.4
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    if luminance > 0.5:
        print ("WHITE")
        return False
        #WHITE
    else:
        #BLACk
        print ("BLACk")
        return True
