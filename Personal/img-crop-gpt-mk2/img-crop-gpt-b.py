import os
from PIL import Image

def detect_black_yellow_border(image, border_height=20):
    """
    Detects if an image has a black and yellow border at the bottom and returns counts and percentages.
    """
    width, height = image.size
    border_area = image.crop((0, height - border_height, width, height))
    
    pixels = border_area.load()
    black_count = 0
    yellow_count = 0
    border_rows = 0

    for y in range(border_height):
        r, g, b = pixels[0, y]  # Check the color of the first pixel in the row
        total_pixels = border_area.width

        # Count black and yellow pixels
        if r < 50 and g < 50 and b < 50:  # Black threshold
            black_count += 1
        elif r > 180 and g > 180 and b < 100:  # Yellow threshold
            yellow_count += 1

        # Calculate percentages for border detection
        black_percentage = (black_count / total_pixels) * 100 if total_pixels > 0 else 0
        yellow_percentage = (yellow_count / total_pixels) * 100 if total_pixels > 0 else 0

        # Check for border conditions
        if black_percentage >= 75 or (black_percentage >= 50 and yellow_percentage >= 0):  # Adjusted yellow threshold
            border_rows += 1
        elif black_percentage > 97 and border_rows > 0:  # Check if the last border row had yellow
            break

    border_detected = border_rows >= 2
    border_height_detected = border_rows if border_detected else 0

    return border_detected, border_height_detected, black_count, yellow_count, black_percentage, yellow_percentage

# Input and output folder paths
input_folder = r'C:\memes\crop-source'
output_folder = r'C:\memes\crop-output'
crop_off_folder = r'C:\memes\crop-off'
crop_none_folder = r'C:\memes\crop-none'
crop_none_vids_folder = r'C:\memes\crop-none-vids'
crop_not_compatible_folder = r'C:\memes\crop-not-compatible'
crop_readme_folder = r'C:\memes\crop-readme'

# Ensure the output folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(crop_off_folder, exist_ok=True)
os.makedirs(crop_none_folder, exist_ok=True)
os.makedirs(crop_none_vids_folder, exist_ok=True)
os.makedirs(crop_not_compatible_folder, exist_ok=True)
os.makedirs(crop_readme_folder, exist_ok=True)

# Initialize counters for recap
total_files_processed = 0
total_output_size = 0
total_images_cropped = 0
total_images_failed = 0
total_videos_copied = 0
total_non_compatible_copied = 0

# Print header
print(f"{'File Name':<40} {'Image (y/n)':<12} {'Border Detected (y/n)':<20} {'Border Height (px)':<18} {'Output Folder'}")

# Process each file in the input folder
for filename in os.listdir(input_folder):
    total_files_processed += 1
    file_path = os.path.join(input_folder, filename)
    
    # Handle non-image and non-video files
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image = Image.open(file_path)

        # Call the function to detect the border
        border_detected, border_height_detected, black_count, yellow_count, black_percentage, yellow_percentage = detect_black_yellow_border(image)

        if border_detected:
            # Crop the border from the image
            cropped_image = image.crop((0, border_height_detected, image.width, image.height))
            cropped_image.save(os.path.join(output_folder, filename))
            # Save the cropped border
            border_image = image.crop((0, 0, image.width, border_height_detected))
            border_image.save(os.path.join(crop_off_folder, filename))
            print(f"{filename:<40} {'y':<12} {'y':<20} {border_height_detected:<18} {output_folder}")
            total_images_cropped += 1
        else:
            print(f"{filename:<40} {'y':<12} {'n':<20} {'n/a':<18} {crop_none_folder}")
            image.save(os.path.join(crop_none_folder, filename))
            total_images_failed += 1

    elif filename.lower().endswith(('.mp4', '.avi', '.mov')):  # Video formats
        print(f"{filename:<40} {'n':<12} {'n/a':<20} {'n/a':<18} {crop_none_vids_folder}")
        os.rename(file_path, os.path.join(crop_none_vids_folder, filename))
        total_videos_copied += 1

    else:  # Non-compatible files
        print(f"{filename:<40} {'n':<12} {'n/a':<20} {'n/a':<18} {crop_not_compatible_folder}")
        os.rename(file_path, os.path.join(crop_not_compatible_folder, filename))
        total_non_compatible_copied += 1

# Recap output
print("-" * 90)
print(f"Total files processed: {total_files_processed}")
print(f"Total output size: {total_output_size:.4f} GB")
print(f"Total images cropped: {total_images_cropped}")
print(f"Total images not cropped: {total_images_failed}")
print(f"Total videos copied: {total_videos_copied}")
print(f"Total non-compatible files copied: {total_non_compatible_copied}")

# Generate CSV report
with open(os.path.join(crop_readme_folder, 'report.csv'), 'w') as report_file:
    report_file.write("File Name,Image (y/n),Border Detected (y/n),Border Height (px),Output Folder\n")
    # Here you would write each processed file's data similarly as you did in the print statements above.

'''This version doesn't generate the error message that version A
was getting, but also doesn't crop any of the images.
womp womp'''