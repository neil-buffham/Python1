from PIL import Image, ImageColor
import csv

def get_closest_color_name(rgb_value):
    # Dictionary of named colors in Pillow
    color_names = ImageColor.colormap
    min_distance = float('inf')
    closest_color = None
    
    # Find the closest color by calculating the Euclidean distance in RGB space
    for name, hex_value in color_names.items():
        r, g, b = ImageColor.getrgb(hex_value)
        distance = ((r - rgb_value[0]) ** 2 + 
                    (g - rgb_value[1]) ** 2 + 
                    (b - rgb_value[2]) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_color = name
    return closest_color

def extract_rgb_values(image_path):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Determine the left, right, center, and 20 pixels from right columns
    left_column = 0
    right_column = width - 1
    center_column = (width // 2) if width % 2 == 1 else (width // 2)
    twenty_from_right_column = width - 21

    # Function to extract RGB data for a specific column
    def get_column_rgb_data(column_index):
        pixel_data = []
        for i in range(30):
            y = height - 1 - i
            rgb = img.getpixel((column_index, y))
            color_name = get_closest_color_name(rgb)
            pixel_data.append((rgb[0], rgb[1], rgb[2], color_name))
        return pixel_data

    # Extract data for left, center, 20 pixels from right, and right columns
    left_data = get_column_rgb_data(left_column)
    center_data = get_column_rgb_data(center_column)
    twenty_from_right_data = get_column_rgb_data(twenty_from_right_column)
    right_data = get_column_rgb_data(right_column)

    # Combine data into rows for CSV output
    all_pixel_data = []
    for i in range(30):
        row = [i + 1] + list(left_data[i]) + list(center_data[i]) + list(twenty_from_right_data[i]) + list(right_data[i])
        all_pixel_data.append(row)

    return all_pixel_data

def save_to_csv(pixel_data, output_path):
    # Write data to CSV
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Pixel Number", 
            "Left Red", "Left Green", "Left Blue", "Left Name",
            "Center Red", "Center Green", "Center Blue", "Center Name",
            "20 Pixels from Right Red", "20 Pixels from Right Green", "20 Pixels from Right Blue", "20 Pixels from Right Name",
            "Right Red", "Right Green", "Right Blue", "Right Name"
        ])
        writer.writerows(pixel_data)

def main():
    # Image path
    image_path = r"C:\memes\detect\test1.jpg"

    # Output CSV file path
    output_path = r"C:\memes\detect\test1_colors.csv"

    # Extract RGB values
    pixel_data = extract_rgb_values(image_path)

    # Save data to CSV
    save_to_csv(pixel_data, output_path)
    print(f"RGB values have been saved to {output_path}")

if __name__ == "__main__":
    main()
