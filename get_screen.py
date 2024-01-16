from PIL import ImageGrab, Image


def on_cropped_img(top_left,bottom_right,dinosaur_Topleft,dinosaur_bottomright):
    dinosaur_Topleft_x = dinosaur_Topleft[0] - top_left[0]
    dinosaur_Topleft_y = dinosaur_Topleft[1] - top_left[1]
    dinosaur_bottomright_x = dinosaur_bottomright[0] - top_left[0]
    dinosaur_bottomright_y = dinosaur_bottomright[1] - top_left[1]

    
    return (dinosaur_Topleft_x,dinosaur_Topleft_y),(dinosaur_bottomright_x,dinosaur_bottomright_y)

def Capture_and_crop_screenshot(top_left,bottom_right,dinosaur_Topleft,dinosaur_bottomright):
    screenshot = ImageGrab.grab()
    crop_coords = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
    cropped_image = screenshot.crop(crop_coords)
    cropped_image.save(f"F:/GitHub/dinosaur_game_bot/screen_shots/cropped_screenshot.png")
    dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img = on_cropped_img(top_left,bottom_right,dinosaur_Topleft,dinosaur_bottomright)
    return dinosaur_Topleft_on_cropped_img , dinosaur_bottomright_on_cropped_img,cropped_image      
    
        
