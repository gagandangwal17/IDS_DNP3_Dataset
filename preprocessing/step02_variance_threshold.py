from sklearn.feature_selection import VarianceThreshold
import pandas as pd
import os

input_dir = 'Updated Dataset'

for dirname, _, filenames in os.walk(input_dir):
    for filename in filenames:
        file_path = os.path.join(dirname, filename)
        
        df = pd.read_csv(file_path)

        # Exclude columns with string values
        numeric_columns = df.select_dtypes(include=['number'])

        # Apply variance threshold
        var_thres = VarianceThreshold(threshold=0)
        var_thres.fit(numeric_columns)
        const_features = [column for column in numeric_columns.columns
                          if column not in numeric_columns.columns[var_thres.get_support()]]
        print(len(const_features))
