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

def crop_image(img, border_height):
    # Crop the image based on the detected border height
    width, height = img.size
    cropped_result = img.crop((0, 0, width, height - border_height))
    cropped_border = img.crop((0, height - border_height, width, height))
    return cropped_result, cropped_border

def process_images(base_path):
    # Paths for directories
    source_path = os.path.join(base_path, "crop-source")
    result_path = os.path.join(base_path, "crop-result")
    off_path = os.path.join(base_path, "crop-off")
    not_comp_path = os.path.join(base_path, "crop-not-comp")
    fail_path = os.path.join(base_path, "crop-fail")
    readme_path = os.path.join(base_path, "crop-readme", "cropping_data.csv")

    # Statistics tracking
    total_files_processed = 0
    images_cropped = 0
    total_border_height = 0
    images_failed = 0

    # Prepare the CSV file
    with open(readme_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([
            "Image name", "Destination folder", "Border height",
            "R val 1", "G val 1", "B val 1",
            "R val 2", "G val 2", "B val 2",
            "R val 3", "G val 3", "B val 3"
        ])

        # Process each file in the source directory
        for filename in os.listdir(source_path):
            file_path = os.path.join(source_path, filename)
            total_files_processed += 1

            # If it's not an image, copy to crop-not-comp
            if not is_image_file(file_path):
                os.rename(file_path, os.path.join(not_comp_path, filename))
                continue

            # Open the image
            try:
                img = Image.open(file_path)
                img = img.convert("RGB")  # Ensure it's in RGB mode
                rgb_values = read_rgb_values(img, column=0, num_rows=30)
                border_height, unique_colors = detect_border(rgb_values)

                if border_height == 0:
                    # If no significant border is found, move to crop-fail
                    os.rename(file_path, os.path.join(fail_path, filename))
                    images_failed += 1
                else:
                    # Crop the image and save results
                    cropped_result, cropped_border = crop_image(img, border_height)
                    cropped_result.save(os.path.join(result_path, filename))
                    cropped_border.save(os.path.join(off_path, filename))
                    
                    # Log data to CSV
                    csvwriter.writerow([
                        filename, "crop-result", border_height,
                        *unique_colors[0], *unique_colors[1], *unique_colors[2]
                    ])
                    
                    images_cropped += 1
                    total_border_height += border_height

                # Close the image to free resources
                img.close()

            except Exception as e:
                # If there is an error processing the image, treat it as a failure
                os.rename(file_path, os.path.join(fail_path, filename))
                images_failed += 1

    # Output statistics
    print(f"Total files processed: {total_files_processed}")
    print(f"Images cropped: {images_cropped}")
    print(f"Average crop height: {total_border_height / images_cropped if images_cropped > 0 else 0:.2f}")
    print(f"Images failed border detection: {images_failed}")

if __name__ == "__main__":
    base_directory = r"C:\memes"
    create_directories(base_directory)
    process_images(base_directory)
'''works okay, but can't catch the yellow all the time. also overcrops sometimes.'''