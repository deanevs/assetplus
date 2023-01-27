"""
Query Ap for all WO filtered by:
    - active 
    - PM
Setup the directories and merge keys
"""

from pathlib import Path
import pandas as pd
import sys
import os

pd.options.display.max_columns = None
pd.options.display.max_rows = None     # displays all rows ... change None to 100 ow whatever number
pd.options.display.width = 1000

# wdir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\Monthly Reports\CNL')
# fname = '20221219 - PM DATA FROM 2016 - ACTIVE.csv'

path_to_file = '/home/dean/Documents/Work/CNL analysis/20221219 - PM DATA FROM 2017.csv'
# filename = '20221219 - PM DATA FROM 2017.csv'
# path = os.path.join('home', 'dean', 'Documents','Work','CNL analysis','20221219 - PM DATA FROM 2017.csv')


# load data
df_pms = pd.read_csv(path_to_file, on_bad_lines='skip')
print(df_pms.head())
print(df_pms.describe())


def convert_risk(r):
    if r == 1:
        return 'HIGH'
    elif r == 2:
        return 'MEDIUM'
    elif r == 3:
        return 'LOW'
    else:
        return 'ERROR'

# clean and filter
df_pms['wo'] = df_pms['wo'].astype('str')
df_pms['asset'] = df_pms['asset'].astype('str')
df_pms.drop(columns=['call_date'], inplace=True)
df_pms.risk = df_pms.risk.apply(convert_risk)
df_pms['wo_substatus'].replace('NOT FOUND', 'COULD NOT LOCATE', inplace=True)
df_pms['wo_substatus'].replace('JOB DONE', 'JOB COMPLETED', inplace=True)
df_pms['wo_substatus'].replace('PM PASS', 'COULD NOT LOCATE', inplace=True)
df_pms = df_pms[df_pms['wo_substatus'].isin(['JOB DONE', 'JOB COMPLETED', 'PM PASS', 'COULD NOT LOCATE'])]

df_pms.sort_values('end_date', ascending=False, inplace=True)

print(df_pms.head(20))
print(df_pms['wo_substatus'].value_counts())
print(f"Number of PMs = {len(df_pms)}")

# group by asset so that we have all pms associated sorted from more recent to past 
grp = df_pms.groupby('asset')

CNL_LIMIT = 2   # sets the trigger to save the asset & pms to the results
main_cnt = 0    # count for unique assets with CNL_LIMIT or more consecutive latest PMs

# create empty dataframe to hold results
df_out = pd.DataFrame()

for name, group in grp:
    # reset flags
    cnl = 0     # counts continuous cnls from first
    
    # variables to determine last group member
    grp_rows = len(group)
    row_cnt = 0

    # iterate over individuals assets jobs
    for idx, row in group.iterrows():
        row_cnt += 1
        last = row_cnt == grp_rows
        if row['wo_substatus'] == 'COULD NOT LOCATE':
            cnl += 1
        elif cnl >= CNL_LIMIT:
            df_out = pd.concat([df_out, group], ignore_index=True)
            main_cnt += 1
            break
        else:   # not CNL and <2 hence skip asset group without saving
            break

print(f"Total assets = {main_cnt}")
df_out.to_excel((wdir / 'CNL_WITH_2_OR_MORE_CONSECUTIVE.xlsx'), index=False)