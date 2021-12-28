import import_data
import pandas as pd
from pathlib import Path
from fuzzywuzzy import fuzz
import operator
import sys
from collections import defaultdict

pd.set_option('display.max_columns', None)  # or as below

pd.set_option("max_rows", None)



data_folder = Path(r"C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN")

columns = ['MODEL','MANUFACTURER','GMDN ID','GMDN NAME']

file_to_open = data_folder / "MODEL - GMDN INVESTIGATION.xlsx"
df = pd.read_excel(file_to_open, index_col=False, sheet_name='MODEL LIST', usecols=columns)
df = df.reindex(['MANUFACTURER','MODEL','GMDN ID','GMDN NAME'], axis=1)


print(df.head())


model_dict = defaultdict(list)
for index, row in df.iterrows():
    model_dict[row['MODEL']].append(row['MANUFACTURER'])

for key, value in model_dict.items():
    print("\nModel:\t{}".format(key))
    print(value)


# list of words to ignore to reduce false positives
remove_list = [' EQUIPMENT', ' HEALTHCARE', ' MEDICAL',' SERVICES',' MEDICAL',' SCIENTIFIC',  ' INSTRUMENTS',
               ' LTD', ' LIMITED', ' LLC', ' UK', ' EUROPE',  ' (UK)', ' SYSTEMS', ' TECHNOLOGIES',
               ' BIOMEDICAL',' LABORATORIES',' TECHNOLOGY',  ' INSTRUMENTATION', ' SYSTEM', ' INTERNATIONAL']


# results = pd.DataFrame(columns=['Model','Ratio', 'Model_R','Partial_P',''])

for model in model_dict.keys():
    for model_lup in model_dict.keys():
        if model == model_lup:
            continue
        model = str(model)
        model_lup = str(model_lup)
        ratio = fuzz.ratio(model, model_lup)
        partial_ratio = fuzz.partial_ratio(model, model_lup)
        token_sort = fuzz.token_sort_ratio(model, model_lup)
        token_set = fuzz.token_set_ratio(model, model_lup)
        if ratio >= 90:
            print("Testing {}".format(model))
            print("{} ratio = {}".format(model_lup, ratio))
            print("{} partial = {}".format(model_lup, partial_ratio))
            print("{} token_sort = {}".format(model_lup, token_sort))
            print("{} token_set = {}".format(model_lup, token_set))
            print("========================================================")



# sort and save
# analysis_df.sort_values(by=['Original','Proposed'])
# save_file = "analysis2.xlsx"
# analysis_df.to_excel(save_file)
# print("Saved to {}".format(save_file))

