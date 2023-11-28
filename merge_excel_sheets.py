import pandas as pd
import os


import os
import pandas as pd
from typing import NoReturn

def merge_excel_files(
        folder_path: str, 
        output_file: str, 
        target_filename: str,
        target_file_format: str) -> NoReturn:
    """
    Merge Excel files from a specified directory that match a target filename pattern.

    Args:
    folder_path (str): The path to the directory containing the Excel files.
    output_file (str): The path including filename where the merged Excel file will be saved.
    target_filename (str): The initial part of the filename to match.
    target_file_format (str): The file format (extension) to match.

    Returns:
    NoReturn: This function does not return any value.
    """

    # Initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # Loop through all files in the specified folder
    for file in os.listdir(folder_path):
        # Check and selects only the file starting with 'target_filename' and ending with 'target_file_format' 
        if file.startswith(target_filename) and file.endswith(target_file_format):
            file_path = os.path.join(folder_path, file)

            try:
                # Read the Excel file into a DataFrame
                data = pd.read_excel(file_path)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue

            # Append the data to the merged_data DataFrame
            merged_data = pd.concat([merged_data, data], ignore_index=True)

    try:
        # Save the merged data to a new Excel file
        merged_data.to_excel(output_file, index=False)
        print(f"Merged data saved to {output_file}")
    except Exception as e:
        print(f"Error saving merged file to {output_file}: {e}")
