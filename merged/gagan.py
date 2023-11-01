import os
import csv

# Specify the folder containing the CSV files
folder_path = os.path.dirname(os.path.abspath(__file__))

def count_rows_in_csv_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', newline='') as csvfile:
                    csvreader = csv.reader(csvfile)
                    num_rows = sum(1 for row in csvreader)
                print(f'File: {file} - Number of Rows: {num_rows}')


count_rows_in_csv_files(folder_path)
