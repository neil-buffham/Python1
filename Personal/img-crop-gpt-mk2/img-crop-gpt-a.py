import os
import shutil
import csv
from PIL import Image

def detect_border(image):
    """
    Detects the height of a black and yellow border at the bottom of the image.
    Returns the height of the detected border and whether it qualifies as a border.
    """
    width, height = image.size
    border_height = 0
    black_rows = 0
    yellow_found = False

    for y in range(height - 1, -1, -1):  # Start from the bottom of the image
        row_black_count = 0
        row_yellow_count = 0
        
        for x in range(width):
            r, g, b = image.getpixel((x, y))
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
            if yellow_percentage > 0:
                yellow_found = True
            black_rows += 1
        elif black_percentage > 0.97 and yellow_found:
            break  # Stop if we hit a non-border row

    # Determine if there are enough rows detected as a border
    if border_height < 2:
        return False, 0  # Not a valid border
    else:
        return True, black_rows

# Input and output folder paths
input_folder = r'C:\memes\crop-source'  # Use raw string to avoid issues with backslashes
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
header = f"{'File Name':<30} {'Image':<6} {'Border Detected':<15} {'Border Height':<15} {'Output Folder'}"
print(header)
print('-' * len(header))

# Process each file in the input folder
for filename in os.listdir(input_folder):
    total_files_processed += 1  # Count each file processed
    file_path = os.path.join(input_folder, filename)
    is_image = filename.lower().endswith(('.jpg', '.jpeg', '.png'))
    is_video = filename.lower().endswith(('.mp4', '.avi', '.mov'))

    if is_image:
        try:
            image = Image.open(file_path)

            # Detect the border
            border_detected, border_height = detect_border(image)
            output_folder_name = ""

            if border_detected:
                print(f"{filename:<30} {'y':<6} {'y':<15} {border_height:<15} {'crop-output'}")
                output_folder_name = output_folder
                total_images_cropped += 1

                # Crop and save images
                cropped_image = image.crop((0, 0, image.width, image.height - border_height))
                cropped_image.save(os.path.join(output_folder, filename))

                # Save the cropped-off portion
                cropped_off_image = image.crop((0, image.height - border_height, image.width, image.height))
                cropped_off_image.save(os.path.join(crop_off_folder, filename))

            else:
                print(f"{filename:<30} {'y':<6} {'n':<15} {'n/a':<15} {'crop-none'}")
                output_folder_name = crop_none_folder
                total_images_not_cropped += 1
                shutil.copy(file_path, os.path.join(crop_none_folder, filename))

            csv_data.append([filename, 'y', 'y' if border_detected else 'n', border_height if border_detected else 'n/a', output_folder_name])

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            shutil.copy(file_path, os.path.join(crop_not_compatible_folder, filename))
            total_non_compatible_copied += 1
            csv_data.append([filename, 'y', 'n', 'n/a', 'crop-not-compatible'])

    elif is_video:
        print(f"{filename:<30} {'n':<6} {'n/a':<15} {'n/a':<15} {'crop-none-vids'}")
        output_folder_name = crop_none_vids_folder
        total_videos_copied += 1
        shutil.copy(file_path, os.path.join(crop_none_vids_folder, filename))
        csv_data.append([filename, 'n', 'n/a', 'n/a', output_folder_name])

    else:
        print(f"{filename:<30} {'n':<6} {'n/a':<15} {'n/a':<15} {'crop-not-compatible'}")
        output_folder_name = crop_not_compatible_folder
        total_non_compatible_copied += 1
        shutil.copy(file_path, os.path.join(crop_not_compatible_folder, filename))
        csv_data.append([filename, 'n', 'n/a', 'n/a', output_folder_name])

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

# Generate CSV report
csv_file_path = os.path.join(crop_readme_folder, 'data_report.csv')
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(['File Name', 'Image', 'Border Detected', 'Border Height', 'Output Folder'])
    # Write data rows
    csv_writer.writerows(csv_data)

print(f"CSV report generated at: {csv_file_path}")


'''This version functions fine, but outputs an error of too many
values when handling images that don't contain a border.'''