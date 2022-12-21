from pathlib import Path
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows= None     # displays all rows ... change None to 100 ow whatever number
pd.options.display.width = 1000

wdir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\Monthly Reports\CNL')
fname = '20221219 - PM DATA FROM 2016 - ACTIVE.csv'
# fname = 'PM_WO_2016.csv'
df = pd.read_csv((wdir / fname))

def convert_risk(r):
    if r == 1: return 'HIGH'
    elif r == 2: return 'MEDIUM'
    elif r == 3: return 'LOW'
    else: return 'ERROR'


df['wo'] = df['wo'].astype('str')
df['asset'] = df['asset'].astype('str')

df.drop(columns=['call_date'], inplace=True)

df.risk = df.risk.apply(convert_risk)

df['wo_substatus'].replace('NOT FOUND', 'COULD NOT LOCATE', inplace=True)
df['wo_substatus'].replace('JOB DONE', 'JOB COMPLETED', inplace=True)
df['wo_substatus'].replace('PM PASS', 'COULD NOT LOCATE', inplace=True)

df = df[df['wo_substatus'].isin(['JOB DONE', 'JOB COMPLETED', 'PM PASS', 'COULD NOT LOCATE'])]

df.sort_values('end_date', ascending=False, inplace=True)
print(df.head(20))

print(df['wo_substatus'].value_counts())
print(f"Number of PMs = {len(df)}")

grp = df.groupby('asset')

CNL_LIMIT = 2
main_cnt = 0

df_out = pd.DataFrame()

for name, group in grp:
    # used to break for loop from inner if
    skip = False
    # counts continuous cnls from first
    cnl = 0
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
        else:
            break

        if last and cnl >= CNL_LIMIT:
            # print(group)
            df_out = pd.concat([df_out, group], ignore_index=True)
            main_cnt += 1

print(f"Total assets = {main_cnt}")
df_out.to_excel((wdir / 'CNL_WITH_2_OR_MORE_CONSECUTIVE.xlsx'), index=False)