import pandas as pd
import numpy as np
from pathlib import Path
from fuzzywuzzy import fuzz
import operator
import sys

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

dir_path = Path(r"C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN")
file_to_open = dir_path / "active_assets_30_06_20.xls"   #"MODEL - GMDN INVESTIGATION.xlsx"
df = pd.read_excel(file_to_open, index_col=False, sheet_name="A")

print(df.iloc[0])

# remove unused columns for anlysis
#drop_cols = ['Modality name', 'Site No', 'Site Name', 'MD Name', 'Installation Date']
#df = df_orig.drop(columns=drop_cols, axis=1)
print("Shape after dropping columns is {}".format(df.shape))

# Get a list of rows by index that do not have a manufacturer
# so that we can check later
manu_missing_values = []
for index, row in df.iterrows():
    if not isinstance(row['Manufacturer'], str):
        manu_missing_values.append(index)

# now remove empty manufacturer rows
df = df[df['Manufacturer'].notnull()]
print("Shape after dropping missing values is {}".format(df.shape))

# now remove duplicate manufacturers
df = df.drop_duplicates('Manufacturer')
print("Shape after dropping missing values is {}".format(df.shape))



# list of words to ignore to reduce false positives
remove_list = [' EQUIPMENT', ' HEALTHCARE', ' MEDICAL',' SERVICES',' MEDICAL',' SCIENTIFIC',  ' INSTRUMENTS',
               ' LTD', ' LIMITED', ' LLC', ' UK', ' EUROPE',  ' (UK)', ' SYSTEMS', ' TECHNOLOGIES',
               ' BIOMEDICAL',' LABORATORIES',' TECHNOLOGY',  ' INSTRUMENTATION', ' SYSTEM', ' INTERNATIONAL']

def remove_name_parts(full_name):
    for word in remove_list:
        full_name = full_name.replace(word,'')
    return full_name


match_to = df['Manufacturer']

added = []
results = []
for index, row in df.iterrows():
    max_ratio = 0
    if row['Manufacturer'] in added:
        continue
    for manufacturer in match_to:
        if manufacturer == row['Manufacturer'] or manufacturer in added:
            continue
        ratio = fuzz.ratio(remove_name_parts(row['Manufacturer']), remove_name_parts(manufacturer))
        if ratio > 90:
            results.append([row['Manufacturer'], manufacturer, ratio])
            added.append(row['Manufacturer'])
            added.append(manufacturer)


print(*results, sep='\n')

# show all rows for each manufacturer
for manufacturer in added:
    print(df[df['Manufacturer'] == manufacturer])









