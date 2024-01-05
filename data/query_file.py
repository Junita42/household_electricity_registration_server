import csv

def get_unique_values(tsv_file_path, column_names):
    unique_values = {col: set() for col in column_names}

    with open(tsv_file_path, 'r') as tsv_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            for col in column_names:
                unique_values[col].add(row[col])

    return unique_values



if __name__ == "__main__":
    tsv_path = './data/Demo_Data/Household.tsv'
    column_names = ['thermal_type']
    unique_values = get_unique_values(tsv_path, column_names)

    for col, values in unique_values.items():
        print(f"Unique values in '{col}': {values}")
    # specific_value = "thermosolar"
    # specific_values = get_specific_values(tsv_path, column_names, specific_value)
