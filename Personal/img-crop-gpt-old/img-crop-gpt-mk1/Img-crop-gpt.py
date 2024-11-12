import os
from PIL import Image

def detect_black_yellow_border(image, border_height=20, black_threshold=50, yellow_threshold=180):
    """
    Detects if an image has a black and yellow border at the bottom and returns counts and percentages.
    """
    width, height = image.size
    border_area = image.crop((0, height - border_height, width, height))
    
    pixels = border_area.load()
    black_count = 0
    yellow_count = 0

    for x in range(border_area.width):
        r, g, b = pixels[x, border_height // 2]
        
        if r < black_threshold and g < black_threshold and b < black_threshold:
            black_count += 1
        elif r > yellow_threshold and g > yellow_threshold and b < 100:
            yellow_count += 1

    total_pixels = border_area.width
    black_ratio = black_count / total_pixels
    yellow_ratio = yellow_count / total_pixels

    # Return whether a border was detected along with counts and percentages
    border_detected = (black_ratio > 0.8 and yellow_ratio > 0.03)
    return border_detected, black_count, yellow_count, black_ratio * 100, yellow_ratio * 100

# Input and output folder paths
input_folder = 'C:\\memes\\cropsource'
output_folder = 'C:\\memes\\cropoutput'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        # Call the updated function to detect the border
        border_detected, black_count, yellow_count, black_percentage, yellow_percentage = detect_black_yellow_border(image)

        if border_detected:
            print(f"Border detected: {filename}")
            # Code to save the cropped image goes here
        else:
            print(f"No border detected: {filename}")
            print(f"Black pixels: {black_count} ({black_percentage:.2f}%)")
            print(f"Yellow pixels: {yellow_count} ({yellow_percentage:.2f}%)")


# Example usage
input_folder = 'C:\\memes\\cropsource'  # Replace with the actual path to the folder containing the images
output_folder = 'C:\\memes\\cropdest'  # Replace with the actual path to the folder where cropped images will be saved
