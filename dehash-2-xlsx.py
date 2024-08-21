import pandas as pd
import json
import argparse

def convert_json_to_excel(json_file, output_file):
    # Load JSON data from file
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    # Extract 'entries' from the data
    entries = json_data.get('entries', [])

    # Convert to DataFrame
    df = pd.DataFrame(entries)

    # Save DataFrame to Excel
    df.to_excel(output_file, index=False)

    print(f"Excel file '{output_file}' created successfully.")

if __name__ == "__main__":
    # ASCII art banner
    banner = r"""
dehash-2-excel
--------------
      by: maz3sec
          https://github.com/maz3sec


* Reformats raw Dehashed JSON data to Excel (XLSX) *

"""

    print(banner)



    # Create argument parser
    parser = argparse.ArgumentParser(description="Convert JSON data to Excel")

    # Add command-line options
    parser.add_argument('-i', '--json_file', help='Path to the input JSON file', required=True)
    parser.add_argument('-o', '--output', help='Path to the output Excel file, XLSX', default='dehashed-output.xlsx')

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the conversion function with specified arguments
    convert_json_to_excel(args.json_file, args.output)
