import os
import pandas as pd

# choose your source path containing .jsons
folder_path = 'XX'

# Name and path of your output .csv
output_csv = 'XX\\output.csv'

dataframes = []

for filename in os.listdir(folder_path):
    if filename.endswith('.jsonl'):
        file_path = os.path.join(folder_path, filename)
        
        df = pd.read_json(file_path, lines=True)
        dataframes.append(df)

combined_df = pd.concat(dataframes)
combined_df.to_csv(output_csv, index=False)
