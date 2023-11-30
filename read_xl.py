import os
import pandas as pd
from typing import List, Dict

def convert_excel_to_json(
    folder_path: str, 
    file_name: str, 
    required_fields: List[str]) -> List[Dict[str, any]]:
    """
    Converts a set of Excel files to JSON format.

    Args:
    folder_path (str): The path to the directory containing the Excel files.
    file_name (str): The base name of the files to be converted.
    required_fields (List[str]): List of column names to be included in the JSON.

    Returns:
    List[Dict[str, any]]: A list of dictionaries where each dictionary represents data from one Excel file.
    """
    gathered_data = []

    for filename in os.listdir(folder_path):
        if filename.startswith(file_name) and filename.endswith('.xlsx'):
            input_file = os.path.join(folder_path, filename)
            df = pd.read_excel(input_file)

            for _, row in df.iterrows():
                data_dict = {field_name: row[field_name] for field_name in required_fields}
                gathered_data.append(data_dict)

    return gathered_data