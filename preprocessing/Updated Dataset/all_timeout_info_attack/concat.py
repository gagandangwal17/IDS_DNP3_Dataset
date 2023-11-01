import os
import pandas as pd

directory_path = os.path.dirname(os.path.abspath(__file__))

csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
print(csv_files)

dfs = []

for file in csv_files:
    file_path = os.path.join(directory_path, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
combined_df.reset_index(drop=True, inplace=True)
combined_df.to_csv(os.path.join(directory_path, 'result_info.csv'), index=False)
