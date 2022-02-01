import pandas as pd

path_to_file = "C:/Users/USER/Documents/Python Scripts/import_data.py/global_terrorism1.csv"
global_terrorism1 = pd.read_csv(path_to_file)
print(global_terrorism1.head())

