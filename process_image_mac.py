# # class Contour:
# #     def __init__(self, coordinates):
# #         self.coordinates = coordinates

# #     def area(self):
# #         return (self.coordinates[2] - self.coordinates[0]) * (self.coordinates[3] - self.coordinates[1])

# #     def boundingBox(self):
# #         return self.coordinates

# # def preprocess_image(image_data):
# #     # Apply a simple binary threshold
# #     threshold_value = 150
# #     binary_image_data = bytes((0 if byte < threshold_value else 255 for byte in image_data))

# #     return binary_image_data

# # def find_contours(binary_image, width, height):
# #     # Convert 1D bytes to 2D list
# #     pixels = [bytearray(binary_image[i:i + width]) for i in range(0, len(binary_image), width)]

# #     # Find contours
# #     contours = []
# #     for y in range(height):
# #         for x in range(width):
# #             if pixels[y][x] == 255:
# #                 contour = trace_contour(pixels, x, y)
# #                 contours.append(Contour(contour))

# #     return contours

# # def trace_contour(pixels, x, y):
# #     contour = []
# #     stack = [(x, y)]

# #     while stack:
# #         current_x, current_y = stack.pop()
# #         if 0 <= current_x < len(pixels[0]) and 0 <= current_y < len(pixels):
# #             if pixels[current_y][current_x] == 255:
# #                 pixels[current_y][current_x] = 0  # Mark the pixel as visited
# #                 contour.append((current_x, current_y))

# #                 stack.extend([
# #                     (current_x + 1, current_y),
# #                     (current_x - 1, current_y),
# #                     (current_x, current_y + 1),
# #                     (current_x, current_y - 1)
# #                 ])

# #     return contour

# # def detect_dinosaur_and_obstacles(contours):
# #     # Extract information about the dinosaur and obstacles
# #     dinosaur_position = None
# #     obstacles_positions = []

# #     for contour in contours:
# #         # Calculate the area of the contour
# #         area = contour.area()

# #         # Set a threshold to filter out small contours (noise)
# #         if area > 100:
# #             # Get the bounding box of the contour
# #             x, y, w, h = contour.boundingBox()

# #             # Check if it's the dinosaur (you might need to adjust this based on your game)
# #             if w > 30 and h > 30:
# #                 dinosaur_position = (x, y, x + w, y + h)
# #             else:
# #                 obstacles_positions.append((x, y, x + w, y + h))

# #     return dinosaur_position, obstacles_positions

# # def crop_and_process_image(input_image, top_left, bottom_right):
# #     # Crop the image based on specified coordinates
# #     cropped_image = input_image.crop((top_left[0], top_left[1], bottom_right[0], bottom_right[1]))

# #     # # Convert PIL Image to bytes
# #     # image_data = cropped_image.tobytes()

# #     # # Preprocess the cropped image
# #     # binary_image = preprocess_image(image_data)

# #     # # Find contours
# #     # width, height = cropped_image.size
# #     # contours = find_contours(binary_image, width, height)

# #     # # Detect the dinosaur and obstacles
# #     # dinosaur_position, obstacles_positions = detect_dinosaur_and_obstacles(contours)

# #     return cropped_image #, dinosaur_position, obstacles_positions

# # # Example usage:
# # from PIL import Image

# # # Load the input image
# # input_image_path = "path/to/input/image.jpg"
# # input_image = Image.open(input_image_path)

# # # Define the top-left and bottom-right coordinates
# # top_left = (10, 20)  # Replace with actual top-left coordinates
# # bottom_right = (200, 300)  # Replace with actual bottom-right coordinates

# # # Process and crop the image
# # cropped_image, dinosaur_position, obstacles_positions = crop_and_process_image(input_image, top_left, bottom_right)

# # # Display the results or save the cropped_image
# # cropped_image.show()
# # print("Dinosaur Position:", dinosaur_position)
# # print("Obstacles Positions:", obstacles_positions)






# import os
# from PIL import Image

# class Contour:
#     def __init__(self, coordinates):
#         self.coordinates = coordinates

#     def area(self):
#         return (self.coordinates[2] - self.coordinates[0]) * (self.coordinates[3] - self.coordinates[1])

#     def boundingBox(self):
#         return self.coordinates

# def preprocess_image(image_path):
#     # Open the image
#     with open(image_path, 'rb') as file:
#         image_data = file.read()

#     # Apply a simple binary threshold
#     threshold_value = 150
#     binary_image_data = bytes((0 if byte < threshold_value else 255 for byte in image_data))

#     return binary_image_data

# def find_contours(binary_image, width, height):
#     # Convert 1D bytes to 2D list
#     pixels = [bytearray(binary_image[i:i + width]) for i in range(0, len(binary_image), width)]

#     # Find contours
#     contours = []
#     for y in range(height):
#         for x in range(width):
#             if pixels[y][x] == 255:
#                 contour = trace_contour(pixels, x, y)
#                 contours.append(Contour(contour))

#     return contours

# def trace_contour(pixels, x, y):
#     contour = []
#     stack = [(x, y)]

#     while stack:
#         current_x, current_y = stack.pop()
#         if 0 <= current_x < len(pixels[0]) and 0 <= current_y < len(pixels):
#             if pixels[current_y][current_x] == 255:
#                 pixels[current_y][current_x] = 0  # Mark the pixel as visited
#                 contour.append((current_x, current_y))

#                 stack.extend([
#                     (current_x + 1, current_y),
#                     (current_x - 1, current_y),
#                     (current_x, current_y + 1),
#                     (current_x, current_y - 1)
#                 ])

#     return contour

# def detect_dinosaur_and_obstacles(contours):
#     # Extract information about the dinosaur and obstacles
#     dinosaur_position = None
#     obstacles_positions = []

#     for contour in contours:
#         # Calculate the area of the contour
#         area = contour.area()

#         # Set a threshold to filter out small contours (noise)
#         if area > 100:
#             # Get the bounding box of the contour
#             x, y, w, h = contour.boundingBox()

#             # Check if it's the dinosaur (you might need to adjust this based on your game)
#             if w > 30 and h > 30:
#                 dinosaur_position = (x, y, x + w, y + h)
#             else:
#                 obstacles_positions.append((x, y, x + w, y + h))

#     return dinosaur_position, obstacles_positions

# def process_and_save_images(input_folder, output_folder, top_left, bottom_right, dinosaur_position):
#     # Create output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)

#     # Process each image in the input folder
#     for filename in os.listdir(input_folder):
#         if filename.endswith(".png") or filename.endswith(".jpg"):
#             input_path = os.path.join(input_folder, filename)
            
#             # Preprocess the image
#             binary_image = preprocess_image(input_path)

#             # Find contours
#             width, height = 640, 480  # Replace with your actual image dimensions
#             contours = find_contours(binary_image, width, height)

#             # Detect the dinosaur and obstacles
#             dinosaur_position, obstacles_positions = detect_dinosaur_and_obstacles(contours)

#             # Crop the image based on specified coordinates
#             image = Image.open(input_path)
#             cropped_image = image.crop((top_left[0], top_left[1], bottom_right[0], bottom_right[1]))

#             # Save the cropped image to the output folder
#             output_path = os.path.join(output_folder, filename)
#             cropped_image.save(output_path)

#             # Print the results
#             print(f"Cropped image saved to: {output_path}")
#             print("Dinosaur Position:", dinosaur_position)
#             print("Obstacles Positions:", obstacles_positions)
#             print("---")

# # Example usage:
# input_folder = "path/to/input/images"
# output_folder = "path/to/output/images"
# top_left = (10, 20)  # Replace with actual top-left coordinates
# bottom_right = (200, 300)  # Replace with actual bottom-right coordinates
# dinosaur_position = (50, 80, 80, 120)  # Replace with actual dinosaur position coordinates

# process_and_save_images(input_folder, output_folder, top_left, bottom_right, dinosaur_position)



# import os

# class Contour:
#     def __init__(self, coordinates):
#         self.coordinates = coordinates

#     def area(self):
#         return (self.coordinates[2] - self.coordinates[0]) * (self.coordinates[3] - self.coordinates[1])

#     def boundingBox(self):
#         return self.coordinates

# def preprocess_image(image_path):
#     # Open the image
#     with open(image_path, 'rb') as file:
#         image_data = file.read()

#     # Apply a simple binary threshold
#     threshold_value = 150
#     binary_image_data = bytes((0 if byte < threshold_value else 255 for byte in image_data))

#     return binary_image_data

# def find_contours(binary_image, width, height):
#     # Convert 1D bytes to 2D list
#     pixels = [bytearray(binary_image[i:i + width]) for i in range(0, len(binary_image), width)]

#     # Find contours
#     contours = []
#     for y in range(height):
#         for x in range(width):
#             if pixels[y][x] == 255:
#                 contour = trace_contour(pixels, x, y)
#                 contours.append(Contour(contour))

#     return contours

# def trace_contour(pixels, x, y):
#     contour = []
#     stack = [(x, y)]

#     while stack:
#         current_x, current_y = stack.pop()
#         if 0 <= current_x < len(pixels[0]) and 0 <= current_y < len(pixels):
#             if pixels[current_y][current_x] == 255:
#                 pixels[current_y][current_x] = 0  # Mark the pixel as visited
#                 contour.append((current_x, current_y))

#                 stack.extend([
#                     (current_x + 1, current_y),
#                     (current_x - 1, current_y),
#                     (current_x, current_y + 1),
#                     (current_x, current_y - 1)
#                 ])

#     return contour

# def detect_dinosaur_and_obstacles(contours):
#     # Extract information about the dinosaur and obstacles
#     dinosaur_position = None
#     obstacles_positions = []

#     for contour in contours:
#         # Calculate the area of the contour
#         area = contour.area()

#         # Set a threshold to filter out small contours (noise)
#         if area > 100:
#             # Get the bounding box of the contour
#             x, y, w, h = contour.boundingBox()

#             # Check if it's the dinosaur (you might need to adjust this based on your game)
#             if w > 30 and h > 30:
#                 dinosaur_position = (x, y, x + w, y + h)
#             else:
#                 obstacles_positions.append((x, y, x + w, y + h))

#     return dinosaur_position, obstacles_positions

# def process_and_save_images(input_folder, output_folder):
#     # Create output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)

#     # Process each image in the input folder
#     for filename in os.listdir(input_folder):
#         if filename.endswith(".png") or filename.endswith(".jpg"):
#             input_path = os.path.join(input_folder, filename)
            
#             # Preprocess the image
#             binary_image = preprocess_image(input_path)

#             # Find contours
#             width, height = 640, 480  # Replace with your actual image dimensions
#             contours = find_contours(binary_image, width, height)

#             # Detect the dinosaur and obstacles
#             dinosaur_position, obstacles_positions = detect_dinosaur_and_obstacles(contours)

#             # Save the processed image to the output folder
#             output_path = os.path.join(output_folder, filename)
#             with open(output_path, 'wb') as file:
#                 file.write(binary_image)

#             # Print the results
#             print(f"Processed image saved to: {output_path}")
#             print("Dinosaur Position:", dinosaur_position)
#             print("Obstacles Positions:", obstacles_positions)
#             print("---")

from PIL import Image

def crop_png(input_path, output_path, topleft, bottomright):
    # Open the PNG image
    img = Image.open(input_path)

    # Crop the image
    cropped_img = img.crop((topleft[0], topleft[1], bottomright[0], bottomright[1]))

    # Save the cropped image
    # cropped_img.save(output_path)
    cropped_img.save(f"{output_path}screenshot_.png")

# Example usage:
input_path = "/Users/Adam/Documents/GitHub/dinosaur_game_bot/screen_shots"
output_path = "/Users/Adam/Documents/GitHub/dinosaur_game_bot/processed_images/"
# left, top, right, bottom = 100, 50, 400, 300

# crop_png(input_path, output_path, left, top, right, bottom)
