# from PIL import ImageGrab, Image


# # # Path to save the screenshots
# # def Capture_screenshot():
# #     save_path = "F:/GitHub/dinosaur_game_bot/screen_shots/"
# #     screenshot = ImageGrab.grab()
# #     screenshot.save(f"{save_path}screenshot.png")
# #     print("Screenshots captured successfully.")


# # Construct the full path to the screenshot
# def Capture_and_crop_screenshot(top_left,bottom_right,dinosaur_Topleft,dinosaur_bottomright):
#     screenshot = ImageGrab.grab()
#     crop_coords = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
#     cropped_image = screenshot.crop(crop_coords)

#     if test_pixels_in_Box(dinosaur_Topleft[0],dinosaur_Topleft[1],dinosaur_bottomright[0],dinosaur_bottomright[1],screenshot):
#         return True
#     else:
#         return False
#     # test_pixel = screenshot.getpixel(dinosaur)
#     # if calculate_luminance(test_pixel): 
#     #     return True
#     # else:
#     #     return False
#     cropped_image.save(f"F:/GitHub/dinosaur_game_bot/screen_shots/cropped_screenshot.png")



# def calculate_luminance(color):
#     # Calculate relative luminance for sRGB color
#     r, g, b = color
#     r = r / 255.0 if r <= 0.03928 else ((r / 255.0 + 0.055) / 1.055) ** 2.4
#     g = g / 255.0 if g <= 0.03928 else ((g / 255.0 + 0.055) / 1.055) ** 2.4
#     b = b / 255.0 if b <= 0.03928 else ((b / 255.0 + 0.055) / 1.055) ** 2.4
#     luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
#     if luminance > 0.5:
#         # print ("WHITE")
#         return False
#         #WHITE
#     else:
#         #BLACk
#         # print ("BLACk")
#         return True

# def test_pixels_in_Box(x1,y1,x2,y2,screenshot):
#     num_black = 0
#     num_white = 0
#     skycolour = "white"
#     for x in range(x1,x2,1):
#         for y in range(y1,y2,1):
#             test_pixel = screenshot.getpixel((x,y))
#             if calculate_luminance(test_pixel): 
#                 num_black += 1
#             else:
#                 num_white += 1
    
#     area = (x2-x1) * (y2-y1)
#     print(f" skycolour = {skycolour} || num_black = {num_black} || num_white = {num_white} || area = {area} % black = {num_black / area}")
#     if num_black >= (area * 0.99):
#         skycolour = "black"
#     elif num_white >= (area * 0.99):
#         skycolour = "white"

#     if num_black >= (area * 0.05) and skycolour == "white":
#         return True
#     elif num_black <= (area * 0.05) and skycolour == "white":
#         return False

#     if num_white >= (area * 0.05) and skycolour == "black":
#         return True
#     elif num_white <= (area * 0.05) and skycolour == "black":
#         return False




from PIL import ImageGrab, Image



        
def Process(dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img,cropped_image):
    if test_pixels_in_Box(dinosaur_Topleft_on_cropped_img[0],dinosaur_Topleft_on_cropped_img[1],dinosaur_bottomright_on_cropped_img[0],dinosaur_bottomright_on_cropped_img[1],cropped_image):
        return True
    else:
        return False
   
def test_pixels_in_Box(x1,y1,x2,y2,cropped_image):
    num_black = 0
    num_white = 0
    skycolour = "white"
    for x in range(x1,x2,1):
        for y in range(y1,y2,1):
            test_pixel = cropped_image.getpixel((x,y))
            if calculate_luminance(test_pixel): 
                num_black += 1
            else:
                num_white += 1
    
    area = (x2-x1) * (y2-y1)
    print(f" skycolour = {skycolour} || num_black = {num_black} || num_white = {num_white} || area = {area} % black = {num_black / area}")
    if num_black >= (area * 0.99):
        skycolour = "black"
    elif num_white >= (area * 0.99):
        skycolour = "white"

    if num_black >= (area * 0.05) and skycolour == "white":
        return True
    elif num_black <= (area * 0.05) and skycolour == "white":
        return False

    if num_white >= (area * 0.05) and skycolour == "black":
        return True
    elif num_white <= (area * 0.05) and skycolour == "black":
        return False


def calculate_luminance(color):
    # Calculate relative luminance for sRGB color
    r, g, b = color
    r = r / 255.0 if r <= 0.03928 else ((r / 255.0 + 0.055) / 1.055) ** 2.4
    g = g / 255.0 if g <= 0.03928 else ((g / 255.0 + 0.055) / 1.055) ** 2.4
    b = b / 255.0 if b <= 0.03928 else ((b / 255.0 + 0.055) / 1.055) ** 2.4
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    if luminance > 0.5:
        # print ("WHITE")
        return False
        #WHITE
    else:
        #BLACk
        # print ("BLACk")
        return True

