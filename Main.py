import csv
import re

def clean_value(value):
    # Clean the text: strip spaces, lowercase and then capitalize where needed
    value = value.strip().lower()
    
    # If it's a time value, remove the "hrs" or any related text and keep the number
    if 'hrs' in value:
        value = re.sub(r'[^\d.]+', '', value)  # Remove non-numeric characters except for the dot

    # Handle the boolean values like 'yes', 'no', etc.
    if value in ['yes', 'no']:
        return value.capitalize()

    # Try converting the value to a float or int
    try:
        if '.' in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        return value.capitalize()  # For text values like names

def process_csv(input_filename, output_filename):
    with open(input_filename, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            cleaned_row = [clean_value(value) for value in row]
            writer.writerow(cleaned_row)

if __name__ == "__main__":
    input_filename = "input.csv"  # Replace with your input CSV file
    output_filename = "output_cleaned.csv"  # Desired output file name

    process_csv(input_filename, output_filename)
    print(f"Cleaned data has been written to {output_filename}")
