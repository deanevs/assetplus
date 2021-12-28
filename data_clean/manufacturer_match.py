import pandas as pd
from pathlib import Path
from fuzzywuzzy import fuzz
import operator
import sys

data_folder = Path(r"C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN")

file_to_open = data_folder / "active_assets_30_06_20.xls"   #"MODEL - GMDN INVESTIGATION.xlsx"
df = pd.read_excel(file_to_open, index_col=False, sheet_name='A')

manu_dict = {}
# make a key value dict for manufacturer and value as number of devices
for manufacturer in df.Manufacturer:
    if manufacturer in manu_dict:
        count = manu_dict[manufacturer] + 1
        manu_dict[manufacturer] = count
    else:
        manu_dict[manufacturer] = 1


# sort by highest number of assets i.e. value
sorted = sorted(manu_dict.items(), key=operator.itemgetter(1))

# list of words to ignore to reduce false positives
remove_list = [' EQUIPMENT', ' HEALTHCARE', ' MEDICAL',' SERVICES',' MEDICAL',' SCIENTIFIC',  ' INSTRUMENTS',
               ' LTD', ' LIMITED', ' LLC', ' UK', ' EUROPE',  ' (UK)', ' SYSTEMS', ' TECHNOLOGIES',
               ' BIOMEDICAL',' LABORATORIES',' TECHNOLOGY',  ' INSTRUMENTATION', ' SYSTEM', ' INTERNATIONAL']


non_str = set()

# create empty dataframe
analysis_df = pd.DataFrame(columns=['Orig','FO', 'Prop','FP'])


ignore = []

counter = 0
for comp in sorted:
    company = str(comp[0])
    if isinstance(company, str):     # MUST BE STRING
        for check in sorted:
            if isinstance(check[0], str):

                partial_company = company
                partial_check = check[0]
                if partial_check == partial_company:    # since matching the same lists, ignore the exact match
                    continue
                for word in remove_list:   # remove all words from name that cause errors
                    if word in partial_company:
                        partial_company = partial_company.replace(word, '')
                    if word in partial_check:
                        partial_check = partial_check.replace(word, '')

                ratio = fuzz.ratio(partial_company, partial_check)
                partial_ratio = fuzz.partial_ratio(partial_company, partial_check)
                token_sort = fuzz.token_sort_ratio(partial_company, partial_check)
                token_set = fuzz.token_set_ratio(partial_company, partial_check)
                if (ratio >= 89 ):  # this seems to give the best indication of reasonable match

                    counter += 1
                    print("Testing {} versus {}".format(comp, check))
                    print("{} ratio = {}".format(partial_company, ratio))
                    print("{} partial = {}".format(partial_company, partial_ratio))
                    print("{} token_sort = {}".format(partial_company, token_sort))
                    print("{} token_set = {}".format(partial_company, token_set))
                    print("========================================================")
                    if int(comp[1]) > int(check[1]):
                        orig = check[0]
                        orig_f = check[1]
                        prop = comp[0]
                        prop_f = comp[1]
                    else:
                        orig = comp[0]
                        orig_f = comp[1]
                        prop = check[0]
                        prop_f = check[1]

                    analysis_df = analysis_df.append({'Orig': orig,'FO': orig_f, 'Prop': prop,'FP': prop_f}, ignore_index=True)
    else:
        non_str.update(company)


print("Number of matches = " + str(counter))

# sort and save
analysis_df.sort_values(by=['Orig','Prop'])
save_file = "analysis_30_06_2020.xlsx"
analysis_df.to_excel(save_file)
print("Saved to {}".format(save_file))

