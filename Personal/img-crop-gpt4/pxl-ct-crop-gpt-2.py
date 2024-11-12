import os
import csv
from PIL import Image

def create_directories(base_path):
    # Create required directories if they don't exist
    directories = [
        "crop-source", "crop-result", "crop-off",
        "crop-not-comp", "crop-readme", "crop-fail"
    ]
    for directory in directories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

def is_image_file(file_path):
    # Check if a file is an image based on its extension
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    return file_path.lower().endswith(valid_extensions)

def read_rgb_values(img, column, num_rows):
    # Read RGB values from the specified column, for the first num_rows from the bottom up
    width, height = img.size
    pixel_values = []
    for i in range(num_rows):
        y = height - 1 - i
        pixel = img.getpixel((column, y))[:3]  # Ignore alpha channel if present
        pixel_values.append(pixel)
    return pixel_values

def detect_border(rgb_values):
    # Detect the border based on the first 30 pixels
    unique_values = []
    for rgb in rgb_values:
        if rgb not in unique_values:
            unique_values.append(rgb)
        if len(unique_values) == 3:
            break

    # Compare the RGB values to the first three unique values
    border_height = 0
    mismatched_count = 0
    for i, rgb in enumerate(rgb_values):
        if rgb not in unique_values:
            mismatched_count += 1
            if mismatched_count == 2:
                border_height = i + 1
                break
        else:
            mismatched_count = 0

    return border_height if border_height > 5 else 0, unique_values[:3]

def process_image(file_path, csvwriter):
    # Open the image
    img = Image.open(file_path)
    img = img.convert("RGB")  # Ensure it's in RGB mode
    width, height = img.size

    # Check pixels from left, center, and right
    left_rgb_values = read_rgb_values(img, column=0, num_rows=30)
    center_rgb_values = read_rgb_values(img, column=width // 2, num_rows=30)
    right_rgb_values = read_rgb_values(img, column=width - 1, num_rows=30)

    left_border_height, left_unique_colors = detect_border(left_rgb_values)
    center_border_height, center_unique_colors = detect_border(center_rgb_values)
    right_border_height, right_unique_colors = detect_border(right_rgb_values)

    # Determine the ideal border height
    border_candidates = [
        (left_border_height, left_unique_colors),
        (center_border_height, center_unique_colors),
        (right_border_height, right_unique_colors),
    ]

    chosen_border_height = 0
    for height, _ in border_candidates:
        if 20 <= height <= 30:
            if (chosen_border_height == 0) or (abs(25 - height) < abs(25 - chosen_border_height)):
                chosen_border_height = height

    # Finalize the chosen border height
    if chosen_border_height > 0:
        chosen_border_height += 2  # Add two pixel rows for the final border
    else:
        chosen_border_height = 0

    # Check for failure conditions
    if chosen_border_height <= 15 or all(height == 0 for height, _ in border_candidates):
        # Copy to the crop-fail folder
        os.rename(file_path, os.path.join("crop-fail", os.path.basename(file_path)))
        return 0, 0, 0  # No valid crop

    # Crop the image
    cropped_result = img.crop((0, 0, width, height - chosen_border_height))
    cropped_border = img.crop((0, height - chosen_border_height, width, height))

    # Save cropped images
    cropped_result.save(os.path.join("crop-result", os.path.basename(file_path)))
    cropped_border.save(os.path.join("crop-off", os.path.basename(file_path)))

    # Log data to CSV
    csvwriter.writerow([
        os.path.basename(file_path), "crop-result", chosen_border_height,
        left_border_height, center_border_height, right_border_height
    ])

    return chosen_border_height, left_border_height, center_border_height, right_border_height

def process_images(base_path):
    # Prepare the CSV file
    readme_path = os.path.join(base_path, "crop-readme", "cropping_data.csv")

    with open(readme_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([
            "Image name", "Destination folder", "Chosen border height",
            "Left border height", "Middle border height", "Right border height"
        ])

        total_files_processed = 0
        images_cropped = 0
        total_crop_height = 0
        images_failed = 0

        # Process each file in the source directory
        for filename in os.listdir(os.path.join(base_path, "crop-source")):
            file_path = os.path.join(base_path, "crop-source", filename)
            total_files_processed += 1

            # If it's not an image, copy to crop-not-comp
            if not is_image_file(file_path):
                os.rename(file_path, os.path.join("crop-not-comp", filename))
                continue

            try:
                chosen_border_height, left_height, center_height, right_height = process_image(file_path, csvwriter)
                if chosen_border_height > 0:
                    images_cropped += 1
                    total_crop_height += chosen_border_height
                else:
                    images_failed += 1

            except Exception as e:
                # Handle any errors that occur during processing
                images_failed += 1

    # Output statistics
    print(f"Total files processed: {total_files_processed}")
    print(f"Images cropped: {images_cropped}")
    print(f"Average crop height: {total_crop_height / images_cropped if images_cropped > 0 else 0:.2f}")
    print(f"Images failed border detection: {images_failed}")

if __name__ == "__main__":
    base_directory = r"C:\memes"
    create_directories(base_directory)
    process_images(base_directory)
