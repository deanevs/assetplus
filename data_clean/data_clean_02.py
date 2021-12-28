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
# dir_path = Path(r"C:\Users\212628255\Box Sync\AssetPlus UK\Imperial\Data Cleaning")
file_to_open = dir_path / "active_assets_30_06_20.xls"   #"MODEL - GMDN INVESTIGATION.xlsx"
df_orig = pd.read_excel(file_to_open, index_col=False) #, sheet_name="CONSOLIDATED")

print(df_orig.iloc[0])

# remove unused columns for anlysis
drop_cols = ['Modality name', 'Site No', 'Site Name', 'MD Name', 'Installation Date']
df_analyse = df_orig.drop(columns=drop_cols, axis=1)
print("Shape after dropping columns is {}".format(df_analyse.shape))

# Get a list of rows by index that do not have a manufacturer
# so that we can check later
manu_missing_values = []
for idx_outer, outer in df_analyse.iterrows():
    if not isinstance(outer['Manufacturer'], str):
        manu_missing_values.append(idx_outer)

# now remove empty manufacturer and models rows
df_analyse = df_analyse[df_analyse['Manufacturer'].notnull()]
df_analyse = df_analyse[df_analyse['Model'].notnull()]
df_analyse.reset_index(drop=True, inplace=True)
print("Shape after dropping missing values is {}".format(df_analyse.shape))

# join manufacturer and model since model is not unique
df_analyse['combined'] = df_analyse[['Manufacturer', 'Model']].astype(str).apply(' : '.join, axis=1)

# now remove duplicate models
df_analyse = df_analyse.drop_duplicates('combined')
print("Shape after dropping duplicate values is {}".format(df_analyse.shape))

# match_to = df_analyse['combined']

# for items in match_to.iteritems():
#     print(items)
# sys.exit()

added = []
results = []
# df_results = pd.DataFrame(columns=['Match1','Match2','Ratio'])
number_rows = len(df_analyse['combined'])
print("Number of rows in loop: {}".format(number_rows))

for idx_outer, outer in df_analyse.iterrows():
    print(idx_outer)
    # init variables for the inner loop
    max_ratio = 90  # min level of matching
    cnt = 0         # counter to know end of loop
    matched = False # used to show only matched items
    temp_holder = ()
    # skip if already done
    if outer['combined'] in added:
        continue
    # now do the internal loop
    for idx_inner, inner in df_analyse.iterrows():
        cnt += 1
        if inner['combined'] == outer['combined'] or inner['combined'] in added:
            continue
        ratio = fuzz.ratio(outer['combined'], inner['combined'])
        if ratio > 90 and ratio > max_ratio:
            max_ratio = ratio
            print("Max ratio = {}".format(max_ratio))
            temp_holder = (idx_outer, idx_inner, max_ratio)
            print(temp_holder)
            matched = True
        if cnt == number_rows and matched is True:  # save/show only the highest match
            print("Here")
            print(df_analyse.iloc[temp_holder[0]])
            print(df_analyse.iloc[temp_holder[1]])
            print("Match: {}%".format(temp_holder[2]))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # df_results = df_results.append({'Match1':temp_holder[0],'Match2':temp_holder[1],'Ratio':temp_holder[2]}, ignore_index=True)
            # results.append(temp_holder)
            added.append(inner['combined'])
            added.append(outer['combined'])


# print(*results, sep='\n')
#
# results_file = "analysis1_16_06_2020.xlsx"
# df_results.to_excel(results_file, index=False)
# print("Saved to {}".format(results_file))










