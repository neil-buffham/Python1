import os
import shutil
import csv
import time
start_time = time.time() # Record the start time before processing
from PIL import Image

def detect_border(image):
    """
    Detects the height of a black and yellow border at the bottom of the image.
    Returns a tuple indicating whether a border is detected, the height of the detected border,
    and the count of valid border rows.
    """
    width, height = image.size
    border_height = 0
    valid_border_rows = 0
    yellow_found = False

    for y in range(height - 1, -1, -1):  # Start from the bottom of the image
        row_black_count = 0
        row_yellow_count = 0
        
        for x in range(width):
            pixel = image.getpixel((x, y))
            if len(pixel) == 3:  # RGB
                r, g, b = pixel
            elif len(pixel) == 4:  # RGBA
                r, g, b, a = pixel  # Ignore alpha
            else:
                continue  # Skip unexpected formats
            
            if r < 50 and g < 50 and b < 50:  # Black pixel
                row_black_count += 1
            elif r > 200 and g > 200 and b < 100:  # Yellow pixel
                row_yellow_count += 1

        total_pixels = width
        black_percentage = row_black_count / total_pixels
        yellow_percentage = row_yellow_count / total_pixels
        
        # Check for border conditions
        if (black_percentage >= 0.75 and black_percentage <= 0.97) or (black_percentage >= 0.50 and yellow_percentage > 0):
            border_height += 1
            valid_border_rows += 1
            if yellow_percentage > 0:
                yellow_found = True
        elif black_percentage > 0.97 and yellow_found:
            break  # Stop if we hit a non-border row

    # Ensure at least 3 valid border rows for it to count as a border
    if valid_border_rows >= 3:
        return True, border_height + 1  # Return increased border height
    else:
        return False, 0  # Not a valid border

# Input and output folder paths
input_folder = r'C:\memes\crop-source'
output_folder = r'C:\memes\crop-output'
crop_off_folder = r'C:\memes\crop-off'
crop_none_folder = r'C:\memes\crop-none'
crop_none_vids_folder = r'C:\memes\crop-none-vids'
crop_not_compatible_folder = r'C:\memes\crop-not-compatible'
crop_readme_folder = r'C:\memes\crop-readme'

# Ensure all output folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(crop_off_folder, exist_ok=True)
os.makedirs(crop_none_folder, exist_ok=True)
os.makedirs(crop_none_vids_folder, exist_ok=True)
os.makedirs(crop_not_compatible_folder, exist_ok=True)
os.makedirs(crop_readme_folder, exist_ok=True)

# Initialize counters and storage for CSV
total_files_processed = 0
total_images_cropped = 0
total_images_not_cropped = 0
total_videos_copied = 0
total_non_compatible_copied = 0
csv_data = []

# Print header for processed files
header = f"{'File Name':<30} {'Image':<6} {'Border Detected':<15} {'Border Height':<15} {'Output Folder':<15} {'Error Message'}"
print(header)
print('-' * len(header))

# Process each file in the input folder
for filename in os.listdir(input_folder):
    total_files_processed += 1
    file_path = os.path.join(input_folder, filename)
    is_image = filename.lower().endswith(('.jpg', '.jpeg', '.png'))
    is_video = filename.lower().endswith(('.mp4', '.avi', '.mov'))
    error_message = ''  # Initialize error message

    if is_image:
        try:
            image = Image.open(file_path)
            border_detected, border_height = detect_border(image)

            if border_detected:
                # Print output with filename truncation
                truncated_filename = f"{filename[:15]}...{filename[-10:]}" if len(filename) > 25 else filename
                print(f"{truncated_filename:<30} {'y':<6} {'y':<15} {border_height:<15} {'crop-output':<15} {'':<15}")
                total_images_cropped += 1

                # Crop and save images (removing one additional line of pixels)
                cropped_image = image.crop((0, 0, image.width, image.height - border_height))
                cropped_image.save(os.path.join(output_folder, filename))

                # Save the cropped-off portion
                cropped_off_image = image.crop((0, image.height - border_height, image.width, image.height))
                cropped_off_image.save(os.path.join(crop_off_folder, filename))

            else:
                truncated_filename = f"{filename[:15]}...{filename[-10:]}" if len(filename) > 25 else filename
                print(f"{truncated_filename:<30} {'y':<6} {'n':<15} {'n/a':<15} {'crop-none':<15} {'':<15}")
                total_images_not_cropped += 1
                shutil.copy(file_path, os.path.join(crop_none_folder, filename))

            csv_data.append([filename, 'y', 'y' if border_detected else 'n', border_height if border_detected else 'n/a', 'crop-output' if border_detected else 'crop-none', error_message])

        except Exception as e:
            error_message = str(e)
            print(f"Error processing {filename}: {error_message}")
            shutil.copy(file_path, os.path.join(crop_not_compatible_folder, filename))
            total_non_compatible_copied += 1
            csv_data.append([filename, 'y', 'n', 'n/a', 'crop-not-compatible', error_message])

    elif is_video:
        print(f"{filename:<30} {'n':<6} {'n/a':<15} {'n/a':<15} {'crop-none-vids':<15} {'':<15}")
        total_videos_copied += 1
        shutil.copy(file_path, os.path.join(crop_none_vids_folder, filename))
        csv_data.append([filename, 'n', 'n/a', 'n/a', 'crop-none-vids', error_message])

    else:
        print(f"{filename:<30} {'n':<6} {'n/a':<15} {'n/a':<15} {'crop-not-compatible':<15} {'':<15}")
        total_non_compatible_copied += 1
        shutil.copy(file_path, os.path.join(crop_not_compatible_folder, filename))
        csv_data.append([filename, 'n', 'n/a', 'n/a', 'crop-not-compatible', error_message])

# End Processing time calculation
elapsed_time = time.time() - start_time

# Print recap of processed files
print("\n" + "-" * 50)
total_size = sum(os.path.getsize(os.path.join(output_folder, f)) for f in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, f)))
total_size_gb = total_size / (1024**3)  # Convert to gigabytes

# Output summary statistics
print(f"Total files processed: {total_files_processed}")
print(f"Total output size (GB): {total_size_gb:.4f}")
print(f"Total images cropped: {total_images_cropped}")
print(f"Total images not cropped: {total_images_not_cropped}")
print(f"Total videos copied: {total_videos_copied}")
print(f"Total non-compatible files copied: {total_non_compatible_copied}")
print(f"Total execution time: {elapsed_time:.2f} seconds")

# Generate CSV report
csv_file_path = os.path.join(crop_readme_folder, 'data_report.csv')
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(['File Name', 'Image', 'Border Detected', 'Border Height', 'Output Folder', 'Error Message'])
    # Write data rows
    csv_writer.writerows(csv_data)

print(f"CSV report generated at: {csv_file_path}")

'''
This version seems to work correctly, formatting the live view well, handling the alpha in .png's R G B A arrangement, and exporting the csv 
nicely without truncating the file names in said csv. 
However, it only works well for pictures with lighter backgrounds. The
code detecting borders needs to be updated.'''