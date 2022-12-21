import pandas as pd
from pathlib import Path
import sys

import sys

data_folder = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20221005 - SPIRE Interface Dates")
nuvolo_file = 'x_nuvo_eam_clinical_devices.xlsx'
must_file = 'must_spire'

df_nuv = pd.read_excel((data_folder / nuvolo_file))

df_ge = pd.read_excel(ge_pm_calc, index_col=False, sheet_name='Asset Data')
df_ap = pd.read_excel(ap_pm_calc, index_col=False, sheet_name='A')

df_ge['STATUS'].replace('In Date','IN DATE',inplace=True)
df_ge['STATUS'].replace('Late','OUT OF DATE',inplace=True)

# list of words to ignore to reduce false positives
# remove_list = [' EQUIPMENT', ' HEALTHCARE', ' MEDICAL',' SERVICES',' MEDICAL',' SCIENTIFIC',  ' INSTRUMENTS',
#                ' LTD', ' LIMITED', ' LLC', ' UK', ' EUROPE',  ' (UK)', ' SYSTEMS', ' TECHNOLOGIES',
#                ' BIOMEDICAL',' LABORATORIES',' TECHNOLOGY',  ' INSTRUMENTATION', ' SYSTEM', ' INTERNATIONAL']

# create empty dataframe
analysis_df = pd.DataFrame(columns=['Asset ID','PM Status GE','PM Status AP','GE Next Date','AP Next Date', 'Install'])

counter = 0
for idx, row in df_ge.iterrows():
    asset_ge = row['ASSET NO']
    status_ge = row['STATUS']
    next_ge = row['NEXT PM']
    install = row['INSTALLATION DATE']

    if status_ge == 'In Date':
        status_ge = 'IN DATE'
    elif status_ge == 'Late':
        status_ge = 'OUT OF DATE'
    else:
        status_ge = 'CHECK'

    for idx1, row1 in df_ap.iterrows():
        asset_ap = row1['Asset no.']
        print(f"Testing {asset_ap} = {asset_ge}")
        if asset_ap == asset_ge:
            print("found")
            status_ap = row1['PM Status']
            next_ap = row1['Date of next PM']
            if status_ap != status_ge:
                analysis_df = analysis_df.append({'Asset ID': asset_ge,'PM Status GE': status_ge,'PM Status AP' : status_ap,'GE Next Date': next_ge,'AP Next Date': next_ap, 'Install': install}, ignore_index=True)
                # print(f"")
            continue


# sys.exit()
#
# counter = 0
# for comp in sorted:
#     company = str(comp[0])
#     if isinstance(company, str):     # MUST BE STRING
#         for check in sorted:
#             if isinstance(check[0], str):
#
#                 partial_company = company
#                 partial_check = check[0]
#                 if partial_check == partial_company:    # since matching the same lists, ignore the exact match
#                     continue
#                 for word in remove_list:   # remove all words from name that cause errors
#                     if word in partial_company:
#                         partial_company = partial_company.replace(word, '')
#                     if word in partial_check:
#                         partial_check = partial_check.replace(word, '')
#
#                 ratio = fuzz.ratio(partial_company, partial_check)
#                 partial_ratio = fuzz.partial_ratio(partial_company, partial_check)
#                 token_sort = fuzz.token_sort_ratio(partial_company, partial_check)
#                 token_set = fuzz.token_set_ratio(partial_company, partial_check)
#                 if (ratio >= 89 ):  # this seems to give the best indication of reasonable match
#
#                     counter += 1
#                     print("Testing {} versus {}".format(comp, check))
#                     print("{} ratio = {}".format(partial_company, ratio))
#                     print("{} partial = {}".format(partial_company, partial_ratio))
#                     print("{} token_sort = {}".format(partial_company, token_sort))
#                     print("{} token_set = {}".format(partial_company, token_set))
#                     print("========================================================")
#                     if int(comp[1]) > int(check[1]):
#                         orig = check[0]
#                         orig_f = check[1]
#                         prop = comp[0]
#                         prop_f = comp[1]
#                     else:
#                         orig = comp[0]
#                         orig_f = comp[1]
#                         prop = check[0]
#                         prop_f = check[1]
#
#                     analysis_df = analysis_df.append({'Orig': orig,'FO': orig_f, 'Prop': prop,'FP': prop_f}, ignore_index=True)
#     else:
#         non_str.update(company)


print("Number of matches = " + str(counter))

print(analysis_df)

# sort and save
# analysis_df.sort_values(by=['Orig','Prop'])

from datetime import datetime

save_file = "pm_check_" + str(datetime.today()) + ".xlsx"
analysis_df.to_excel(save_file)
print("Saved to {}".format(save_file))

