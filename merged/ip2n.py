import pandas as pd
import os

def to_numeric(s):
    try:
        return int(''.join(s.split('-')).replace('.', ''))
    except:
        return s  # return the original string if there's an error in conversion

# Path to the dataset directory
input_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through each file in each folder
for dirname, _, filenames in os.walk(input_dir):
    for filename in filenames:
        file_path = os.path.join(dirname, filename)

        print(f"Processing file: {file_path}")

        try:
            df = pd.read_csv(file_path)

            # Correcting the column names
            for col in ["flow ID", " source IP", " destination IP"]:
                if col in df.columns:
                    df[col] = df[col].astype(str).apply(to_numeric)

            # Save the modified DataFrame back to its corresponding file
            df.to_csv(file_path, index=False)
            print(f"Processed: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

print("IP strings have been successfully replaced with numeric IPs!")
