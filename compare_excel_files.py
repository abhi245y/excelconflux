import pandas as pd
import pprint

def compare_files(file1, file2, file1_field, file2_filed):
    # Read the Excel files into Pandas dataframes
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    field_a = df1[file1_field]
    field_b = df2[file1_field]

    # Check if all data from file1 are present in file2
    is_all_present = field_a.isin(field_b).all()

    if is_all_present:
        return True, []
    else:
        return Flase, sorted(bundle_codes1[~field_a.isin(field_b)], reverse=True)