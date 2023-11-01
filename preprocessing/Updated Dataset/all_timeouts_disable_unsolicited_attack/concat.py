import pandas as pd
import glob
import os

directory_path = os.path.dirname(os.path.abspath(__file__))
csv_pattern = os.path.join(directory_path, "*.csv")
csv_files = glob.glob(csv_pattern)
dfs = []
files_to_delete = []

for file in csv_files:
    # Read the CSV file and get its number of columns
    df = pd.read_csv(file, header=0)
    
    num_columns = df.shape[1]
    
    if num_columns == 85:
        # If the file has 85 columns, mark it for deletion
        files_to_delete.append(file)
    else:
        dfs.append(df)

# Delete files with 85 columns
for file in files_to_delete:
    os.remove(file)
    print(f"File {os.path.basename(file)} with 85 columns has been deleted.")

# Combine the remaining files
combined_df = pd.concat(dfs, ignore_index=True)

output_csv = os.path.join(directory_path, 'combined_disable_unsolicited.csv')

combined_df.to_csv(output_csv, index=False)

print(f'Combined data saved to {output_csv}\nTotal number of rows: {len(combined_df)}')
