import os
from PIL import Image

def detect_black_yellow_border(image, black_threshold=50):
    """
    Detects the height of a black border at the bottom of the image.
    Returns the height of the black border and counts of black pixels.
    """
    width, height = image.size
    border_height = 0
    black_pixel_rows = 0
    
    # Check the bottom pixels to find the height of the black border
    for y in range(height - 1, -1, -1):  # Start from the bottom of the image
        row_black_count = 0
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            # Check if the pixel is black
            if r < black_threshold and g < black_threshold and b < black_threshold:
                row_black_count += 1
        
        # Calculate the percentage of black pixels in this row
        if row_black_count / width > 0.75:  # 75% black pixels
            border_height += 1
            black_pixel_rows += row_black_count
        else:
            # Stop checking if we encounter a non-black row
            break

    # Return the detected border height and total black pixels detected
    return border_height, black_pixel_rows

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

        # Call the updated function to detect the border height
        border_height, black_pixel_count = detect_black_yellow_border(image)

        if border_height > 0:
            print(f"Border detected: {filename}")
            print(f"Detected border height: {border_height} pixels")
            
            # Crop the image to remove the detected black border
            cropped_image = image.crop((0, 0, image.width, image.height - border_height))
            
            # Save the cropped image to the output folder
            output_path = os.path.join(output_folder, filename)  # Use the original filename
            cropped_image.save(output_path)
            print(f"Cropped image saved: {output_path}")
        else:
            print(f"No border detected: {filename}")
            print(f"Total black pixels counted: {black_pixel_count}")

