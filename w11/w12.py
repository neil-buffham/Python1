running = True
lowest = 1000
lowest_words = ""
lowest_year = ""
highest_words = ""
highest_year = ""
query_year = ""
highest = 0
min_dataset_year = 5000
max_dataset_year = 0
closest_year = None
close_ranking = float('inf')

with open('w11/life-expectancy.csv') as life_data:

    # First loop to find overall lowest and highest values
    line_counter = 1
    for line in life_data:
        output = line.strip()
        output = output.split(',')
        if line_counter > 1:  # Skip header row
            age_val = float(output[3])
            # Getting least and greatest values
            if lowest > age_val:
                lowest = age_val
                lowest_words = output[0]
                lowest_year = output[2]
            if highest < age_val:
                highest = age_val
                highest_words = output[0]
                highest_year = output[2]
            if int(output[2]) > max_dataset_year:
                max_dataset_year = int(output[2])
            if int(output[2]) < min_dataset_year:
                min_dataset_year = int(output[2])
        line_counter += 1

    print(f'The overall max life expectancy is: {highest} from {highest_words} in {highest_year}')
    print(f'The overall min life expectancy is: {lowest} from {lowest_words} in {lowest_year}')

    print()
    print(f'This dataset includes data within the years {min_dataset_year} to {max_dataset_year}.')
    print(f'Not all years are populated.')
    print()

    # Querying for a specific year
    query_year = int(input("Enter the year of interest: "))
    
    # Reset variables for the second calculation
    lowest = 1000
    lowest_words = ""
    lowest_year = ""
    highest_words = ""
    highest_year = ""
    highest = 0

    # Reset the file pointer to the beginning
    # Reset the file pointer to the beginning
    life_data.seek(0)
    line_counter = 1
    
    for line in life_data:
        output = line.strip()
        output = output.split(',')
        if line_counter > 1:  # Skip the header row
            current_year = int(output[2])
            distance = abs(current_year - query_year)
    
            # Check if this year is closer than the current closest
            if distance < close_ranking:
                close_ranking = distance
                closest_year = current_year
    
            # Process data for the specific query year
            if current_year == query_year:
                age_val = float(output[3])
                if lowest > age_val:
                    lowest = age_val
                    lowest_words = output[0]
                    lowest_year = output[2]
                if highest < age_val:
                    highest = age_val
                    highest_words = output[0]
                    highest_year = output[2]
    
        line_counter += 1
    
    # Print the results
    print()
    if lowest == 1000 and highest == 0:  # No matching records found
        print(f"No data found for the year {query_year}.")
    print(f"The closest year was: {closest_year}")
    if lowest != 1000 and highest != 0:
        print(f'The overall max life expectancy is: {highest} from {highest_words}')
        print(f'The overall min life expectancy is: {lowest} from {lowest_words}')
