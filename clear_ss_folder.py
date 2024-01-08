import os

def clear_screenshot_folder(folder_path):
    try:
        # Get the list of files in the folder
        files = os.listdir(folder_path)
        
        # Iterate through each file and remove it
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        print(f"Contents of {folder_path} cleared successfully.")
    except Exception as e:
        print(f"Error clearing contents: {e}")

# Specify the path to the screenshot folder
screenshot_folder_path = "F:\GitHub\dinosaur_game_bot\screen_shots"

# Call the function to clear the screenshot folder
clear_screenshot_folder(screenshot_folder_path)
