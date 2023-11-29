import pandas as pd
from typing import Tuple, List

def compare_files(file1: str, file2: str, file1_field: str, file2_field: str) -> Tuple[bool, List[str]]:
    """
    Compares two Excel files to check if all values in a specific field of file1 are present in file2.

    Args:
    file1 (str): Path to the first Excel file.
    file2 (str): Path to the second Excel file.
    file1_field (str): The field name in the first file to compare.
    file2_field (str): The field name in the second file to compare.

    Returns:
    Tuple[bool, List[str]]: A tuple containing a boolean indicating if all values are present,
                             and a list of values from file1 not found in file2.
    """
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    field_a = df1[file1_field]
    field_b = df2[file2_field]

    is_all_present = field_a.isin(field_b).all()

    if is_all_present:
        return True, []
    else:
        missing_values = sorted(field_a[~field_a.isin(field_b)].unique(), reverse=True)
        return False, missing_values
