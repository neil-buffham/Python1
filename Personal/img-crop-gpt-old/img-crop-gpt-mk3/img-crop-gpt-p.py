import os
import shutil
import csv
import time
from PIL import Image

start_time = time.time()  # Record the start time before processing

def is_tight_yellow(r, g, b):
    """Check if the given RGB values match the tight definition of yellow."""
    return (140 <= r <= 255) and (170 <= g <= 210) and (45 <= b <= 100)

def detect_border(image):
    """
    Detects the height of a black and yellow border at the bottom of the image.
    Returns a tuple indicating whether a border is detected and the initial height of the detected border.
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
            elif r > 200 and g > 200 and b < 100:  # Yellow pixel (loose criteria)
                row_yellow_count += 1

        total_pixels = width
        black_percentage = row_black_count / total_pixels
        yellow_percentage = row_yellow_count / total_pixels

        # Check for initial border conditions
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

def second_scan(image, initial_border_height):
    """
    Perform a second scan on the image to refine the border detection.
    The scan starts halfway up the detected border or 8 pixels, whichever is less.
    """
    width, height = image.size
    refined_border_height = 0
    start_y = height - min(initial_border_height // 2, 8)
    b2_black_percentage = 'n/a'
    b2_yellow_percentage = 'n/a'
    b2_other_percentage = 'n/a'

    for y in range(height - 1, start_y - 1, -1):
        row_black_count = 0
        row_yellow_count = 0
        total_pixels = width

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
            elif is_tight_yellow(r, g, b):  # Tight yellow
                row_yellow_count += 1

        black_percentage = row_black_count / total_pixels
        yellow_percentage = row_yellow_count / total_pixels
        other_percentage = 1.0 - (black_percentage + yellow_percentage)

        # Update the percentages for the last row if the criteria are met
        b2_black_percentage = f"{black_percentage:.2%}"
        b2_yellow_percentage = f"{yellow_percentage:.2%}"
        b2_other_percentage = f"{other_percentage:.2%}"

        # Adjusted condition: Must have 75% black or tight yellow, and yellow can't exceed 45%
        if black_percentage + yellow_percentage >= 0.75 and yellow_percentage <= 0.45:
            refined_border_height += 1
        else:
            break

    return refined_border_height + 1, b2_black_percentage, b2_yellow_percentage, b2_other_percentage  # Add one more line

# Input and output folder paths
input_folder = r'C:\memes\crop-source'
output_folder = r'C:\memes\crop-output'
crop_off_folder = r'C:\memes\crop-off'
crop_none_folder = r'C:\memes\crop-none'
crop_none_vids_folder = r'C:\memes\crop-none-vids'
crop_not_compatible_folder = r'C:\memes\crop-not-compatible'
crop_readme_folder = r'C:\memes\crop-readme'
crop_tall_folder = r'C:\memes\crop-tall'
crop_tall_off_folder = r'C:\memes\crop-tall-off'
crop_fail1_folder = r'C:\memes\crop-fail1'

# Ensure all output folders exist
for folder in [output_folder, crop_off_folder, crop_none_folder, crop_none_vids_folder, 
               crop_not_compatible_folder, crop_readme_folder, crop_tall_folder, 
               crop_tall_off_folder, crop_fail1_folder]:
    os.makedirs(folder, exist_ok=True)

# Initialize counters and storage for CSV
total_files_processed = 0
total_images_cropped = 0
total_images_not_cropped = 0
total_videos_copied = 0
total_non_compatible_copied = 0
csv_data = []

# Print header for processed files
header = f"{'File Name':<30} {'Image':<6} {'Border1':<10} {'Border1 Height':<15} {'Border2':<10} {'B2 Black':<10} {'B2 Yellow':<10} {'B2 Other':<10}"
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
            border1_pass, initial_border_height = detect_border(image)
            border2_height = 'n/a'
            b2_black_percentage = 'n/a'
            b2_yellow_percentage = 'n/a'
            b2_other_percentage = 'n/a'

            if border1_pass:
                # Perform second scan to refine the border
                border2_height, b2_black_percentage, b2_yellow_percentage, b2_other_percentage = second_scan(image, initial_border_height)
                
                # Determine the output folder based on final border height
                if border2_height > 25:
                    output_dest = crop_tall_folder
                    off_dest = crop_tall_off_folder
                else:
                    output_dest = output_folder
                    off_dest = crop_off_folder

                # Crop and save images
                cropped_image = image.crop((0, 0, image.width, image.height - border2_height))
                cropped_image.save(os.path.join(output_dest, filename))

                # Save the cropped-off portion
                cropped_off_image = image.crop((0, image.height - border2_height, image.width, image.height))
                cropped_off_image.save(os.path.join(off_dest, filename))

                total_images_cropped += 1

            else:
                total_images_not_cropped += 1
                shutil.copy(file_path, os.path.join(crop_none_folder, filename))

            # Prepare values for printing and logging
            border1_result = 'pass' if border1_pass else 'fail'
            truncated_filename = f"{filename[:15]}...{filename[-10:]}" if len(filename) > 25 else filename

            # Print the results for each file
            print(f"{truncated_filename:<30} {'y':<6} {border1_result:<10} {initial_border_height:<15} {border2_height:<10} {b2_black_percentage:<10} {b2_yellow_percentage:<10} {b2_other_percentage:<10}")

            # Log the data in the CSV report
            csv_data.append([filename, 'y', border1_result, initial_border_height, border2_height, 
                             b2_black_percentage, b2_yellow_percentage, b2_other_percentage])

        except Exception as e:
            error_message = str(e)
            shutil.copy(file_path, os.path.join(crop_not_compatible_folder, filename))
            total_non_compatible_copied += 1
            csv_data.append([filename, 'y', 'fail', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a'])

    elif is_video:
        print(f"{filename:<30} {'n':<6} {'n/a':<10} {'n/a':<15} {'n/a':<10} {'n/a':<10} {'n/a':<10} {'n/a':<10}")
        total_videos_copied += 1
        shutil.copy(file_path, os.path.join(crop_none_vids_folder, filename))
        csv_data.append([filename, 'n', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a'])

    else:
        shutil.copy(file_path, os.path.join(crop_not_compatible_folder, filename))
        total_non_compatible_copied += 1
        csv_data.append([filename, 'n', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a'])

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
    csv_writer.writerow(['File Name', 'Image', 'Border1', 'Border1 Height', 'Border2', 'B2 Black', 'B2 Yellow', 'B2 Other'])
    # Write data rows
    csv_writer.writerows(csv_data)

print(f"CSV report generated at: {csv_file_path}")
'''This version works alrigt, and added some diagnostic columns. Still fails at around 9% though.'''