import os
import shutil
import csv
import time
start_time = time.time()  # Record the start time before processing
from PIL import Image

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

        # Must have 95% black or tight yellow, and yellow can't exceed 45%
        if black_percentage + yellow_percentage >= 0.95 and yellow_percentage <= 0.45:
            refined_border_height += 1
        else:
            break

    return refined_border_height + 1  # Add one more line

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
            border_detected, initial_border_height = detect_border(image)

            if border_detected:
                # Second scan for refining the border
                final_border_height = second_scan(image, initial_border_height)
                
                # Add one more line of pixels
                final_border_height += 1

                # Determine the output folder based on final border height
                if final_border_height > 25:
                    output_dest = crop_tall_folder
                    off_dest = crop_tall_off_folder
                else:
                    output_dest = output_folder
                    off_dest = crop_off_folder

                # Crop and save images
                cropped_image = image.crop((0, 0, image.width, image.height - final_border_height))
                cropped_image.save(os.path.join(output_dest, filename))

                # Save the cropped-off portion
                cropped_off_image = image.crop((0, image.height - final_border_height, image.width, image.height))
                cropped_off_image.save(os.path.join(off_dest, filename))

                # Print and log results
                truncated_filename = f"{filename[:15]}...{filename[-10:]}" if len(filename) > 25 else filename
                print(f"{truncated_filename:<30} {'y':<6} {'y':<15} {final_border_height:<15} {output_dest:<15} {'':<15}")
                total_images_cropped += 1

            else:
                truncated_filename = f"{filename[:15]}...{filename[-10:]}" if len(filename) > 25 else filename
                print(f"{truncated_filename:<30} {'y':<6} {'n':<15} {'n/a':<15} {'crop-none':<15} {'':<15}")
                total_images_not_cropped += 1
                shutil.copy(file_path, os.path.join(crop_none_folder, filename))

            csv_data.append([filename, 'y', 'y' if border_detected else 'n', 
                             final_border_height if border_detected else 'n/a', 
                             output_dest if border_detected else 'crop-none', 
                             error_message])

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

'''This functions fine for up to about seven rows of pixels, but fails to crop the whole border.'''