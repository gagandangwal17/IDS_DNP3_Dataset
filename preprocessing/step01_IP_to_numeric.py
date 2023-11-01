import pandas as pd
import os

def to_numeric(s):
    try:
        return int(''.join(s.split('-')).replace('.', ''))
    except:
        return s  # return original string if there's an error in conversion

# Path to the dataset directory
input_dir = 'Updated Dataset'

# Loop through each file in each folder
for dirname, _, filenames in os.walk(input_dir):
    for filename in filenames:
        file_path = os.path.join(dirname, filename)
        
        df = pd.read_csv(file_path)
        
        # Correcting the column names
        for col in ["Flow ID", "Src IP", "Dst IP"]:
            if col in df.columns:
                df[col] = df[col].astype(str).apply(to_numeric)
        
        # Save the modified DataFrame back to its corresponding file
        df.to_csv(file_path, index=False)

print("IP strings have been successfully replaced with numeric IPs!")
