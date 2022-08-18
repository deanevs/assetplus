from pathlib import Path
import pandas as pd
import sys

df = pd.read_excel((Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20220817 - CNL Last 3Y') / '20221708-STUART_CNL.xlsx'))
# print(df)

df.sort_values('END DATE', ascending=False, inplace=True)
df['WO NUM'] = df['WO NUM'].astype('str')

grp = df.groupby('ASSET ID')

cnt = 0
CNL_LIMIT = 3
main_cnt = 0

for name, group in grp:
    # used to break for loop from inner if
    skip = False
    # counts continuous cnls from first
    cnl = 0
    # variables to determine last group member
    lth = len(group)
    lth_cnt = 0

    # iterate over individuals assets jobs
    for idx, row in group.iterrows():
        lth_cnt += 1
        last = lth_cnt == lth
        if row.STATUS == 'COULD NOT LOCATE':
            cnl += 1
        elif cnl >= CNL_LIMIT:
            print('\ngroup')
            main_cnt += 1
            skip = True
        else: skip = True

        if skip: break

        if last and cnl >= CNL_LIMIT:
            print('\ngroup')
            main_cnt += 1

print(f"Total assets = {main_cnt}")





    # cnt += 1
    # if cnt == 50:
    #     break
