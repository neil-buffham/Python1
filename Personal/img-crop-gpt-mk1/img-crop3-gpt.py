import os
import shutil
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
cropoff_folder = 'C:\\memes\\cropoff'  # New folder for cropped-off portions
fail_folder = 'C:\\memes\\fail'  # New folder for failed detections
non_images_folder = 'C:\\memes\\non_images'  # New folder for non-image files

# Ensure the output folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(cropoff_folder, exist_ok=True)
os.makedirs(fail_folder, exist_ok=True)
os.makedirs(non_images_folder, exist_ok=True)

# Process each file in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # If it's an image file, process it
        image = Image.open(file_path)

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
            
            # Save the cropped-off portion of the image
            cropped_off_image = image.crop((0, image.height - border_height, image.width, image.height))
            cropped_off_path = os.path.join(cropoff_folder, filename)  # Use the original filename
            cropped_off_image.save(cropped_off_path)
            print(f"Cropped-off portion saved: {cropped_off_path}")
        else:
            print(f"No border detected: {filename}")
            print(f"Total black pixels counted: {black_pixel_count}")
            
            # Save a complete copy of the image in the fail folder
            fail_path = os.path.join(fail_folder, filename)  # Use the original filename
            image.save(fail_path)
            print(f"Failed detection image saved: {fail_path}")

    else:
        # If it's a non-image file, copy it to the non-images folder
        shutil.copy(file_path, os.path.join(non_images_folder, filename))
        print(f"Non-image file copied: {filename}")
