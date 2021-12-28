
import pandas as pd
from pathlib import Path
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
import sys
import analysis

pd.set_option('max_columns', None)
pd.set_option('max_rows', None)
pd.set_option('display.width', 5000)

# Make the graphs a bit prettier, and bigger
# pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)


data_folder = Path(r"C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN")

file_to_open = data_folder / "MODEL - GMDN INVESTIGATION.xlsx"
# file_to_open = data_folder / "test_data.xlsx"
df = pd.read_excel(file_to_open, index_col=False, sheet_name='MODEL LIST')

counts = df['MANUFACTURER'].value_counts()
print(counts[:20])

plt.figure()
counts[:20].plot.bar()

# get excel column to list
raw = df['MANUFACTURER'].tolist()
no_blanks = [x for x in raw if x]   # remove blanks
all_strings = list(map(str, no_blanks))  # convert non-strings to strings
unique_manufacturers = set(all_strings)     # get unique only

# create dictionary with key = manufacturer, value = no. occurrences
manu_dict = {}
for manufacturer in all_strings:
    if manufacturer in manu_dict:
        # print("Adding {}".format(manufacturer))
        count = manu_dict[manufacturer] + 1
        manu_dict[manufacturer] = count
    else:
        manu_dict[manufacturer] = 1

columns = ['Manufacturer','Count', 'Match 1', 'Count 1', '% 1', 'Match 2', 'Count 2', '% 2', 'Match 3', 'Count 3', '% 3']

# init dataframe
df_results = pd.DataFrame(columns= columns)

for manufacturer in unique_manufacturers:
    result = process.extract(manufacturer, unique_manufacturers, limit=4)
    result = fuzz.ratio
    df_results = df_results.append({
        'Manufacturer': manufacturer,
        'Count': manu_dict[manufacturer],
        'Match 1': result[1][0],
        'Count 1' : manu_dict[result[1][0]],
        '% 1': result[1][1],
        'Match 2': result[2][0],
        'Count 2': manu_dict[result[2][0]],
        '% 2': result[2][1],
        'Match 3': result[3][0],
        'Count 3': manu_dict[result[3][0]],
        '% 3': result[3][1]},
        ignore_index=True)

# now sort the dataframe with the highest scores first
df_results = df_results.sort_values(by=['% 1', '% 2', '% 3'], ascending=False)

analysis.analyse(df_results)



