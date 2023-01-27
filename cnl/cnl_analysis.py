"""
Query Ap for all WO filtered by:
    - active 
    - PM
Setup the directories and merge keys
"""

from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os

pd.options.display.max_columns = None
pd.options.display.max_rows = None     # displays all rows ... change None to 100 ow whatever number
pd.options.display.width = 1000

# wdir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\Monthly Reports\CNL')
# fname = '20221219 - PM DATA FROM 2016 - ACTIVE.csv'
path_to_file = '/home/dean/Documents/Work/CNL analysis/PM WO SINCE 2017.csv'


def main():
    # load data
    df = pd.read_csv(path_to_file, on_bad_lines='skip')

    df = df.rename(
        columns={'WO_NUM': 'wo', 'ASSET_ID': 'asset', 'DESCRIPTION': 'name', 'SERIAL': 'serial', 'MODEL': 'model',
                 'MANUFACTURER': 'manufacturer', 'GMDN_NO': 'gmdn', 'EQ_NUM': 'equip', 'DEPT': 'dept', 'SITE': 'site',
                 'CALL DATE': 'call_date', 'END DATE': 'end_date', 'TECH_DEPT': 'tech_dept', 'TECHNICIAN': 'tech',
                 'WO_SUB-STATUS': 'status', 'RISK': 'risk', 'INSTALL': 'install'})

    df.drop(columns=['WO_TYPE', 'WO_SUB-TYPE'], inplace=True)

    # clean and filter
    df['wo'] = df['wo'].astype('str')
    df['asset'] = df['asset'].astype('str')
    df.risk = df.risk.apply(convert_risk)
    df['status'].replace('NOT FOUND', 'COULD NOT LOCATE', inplace=True)
    df['status'].replace('JOB DONE', 'JOB COMPLETED', inplace=True)
    df['status'].replace('PM PASS', 'COULD NOT LOCATE', inplace=True)
    df = df[df['status'].isin(['JOB DONE', 'JOB COMPLETED', 'PM PASS', 'COULD NOT LOCATE'])]

    # make column with the first of this month
    this_month_first = datetime(datetime.today().year, datetime.today().month, 1).date()
    df['this_month_first'] = pd.to_datetime(this_month_first)

    # make column for first of end date month
    df['end_date_first'] = df.end_date.to_numpy().astype('datetime64[M]')

    # get month difference
    df['delta_months'] = ((df.this_month_first - df.end_date_first) / np.timedelta64(1, 'M')).astype(int)

    df.sort_values('end_date', ascending=False, inplace=True)

    print(df.head(20))
    print(df['status'].value_counts())
    print(f"Number of PMs = {len(df)}")

    # group by asset so that we have all pms associated sorted from more recent to past
    grp = df.groupby('asset')

    # create empty dataframe to hold results
    df_follow_up = pd.DataFrame()
    df_deactivation = pd.DataFrame()

    # counters
    cnt_followup = 0
    cnt_deactivate = 0
    cnt_ignore = 0

    for name, group in grp:
        # reset flags
        cnl_cnt = 0  # counts continuous cnls from first

        # variables to determine last group member
        grp_rows = len(group)
        row_cnt = 0
        fg_followup = False

        # iterate over individuals assets jobs
        for idx, row in group.iterrows():
            row_cnt += 1
            fg_first_row = row_cnt == 1
            fg_last_row = row_cnt == grp_rows  # set last flag
            fg_cnl = row['status'] == 'COULD NOT LOCATE'   # set cnl flag

            # only look at 6 months for first row
            if fg_first_row:
                # reset flags
                fg_followup = False

                if row['delta_months'] == 6 and fg_cnl:
                    # print(row)
                    fg_followup = True
                    cnl_cnt += 1
                else:
                    cnt_ignore += 1
                    break    # get next group

            # not first row but already qualified and is a cnl
            elif fg_followup and fg_cnl:   # ALREADY CNL PLUS CNL
                cnl_cnt += 1    # increment cnl count
                if cnl_cnt == 3:
                    # print(f'DEACTIVATE {row.asset}')
                    # print(row)
                    df_deactivation = pd.concat([df_deactivation, group], ignore_index=True)
                    cnt_deactivate += 1
                    break

            # not cnl but the first qualified hence add to followup and terminate group
            elif fg_followup:   # not CNL so end it here
                # print(f'FOLLOWUP {row.asset}')
                cnt_followup += 1
                df_follow_up = pd.concat([df_follow_up, group], ignore_index=True)
                break
            # shouldn't get here
            else:
                print('I am illegally here')
                break

    print(f"DEACTIVATE = {cnt_deactivate}")
    print(f"FOLLOWUP = {cnt_followup}")
    print(f"IGNORE = {cnt_ignore}")

    df_deactivation.to_excel('DEACTIVATION.xlsx', index=False)
    df_follow_up.to_excel('FOLLOWUP.xlsx', index=False)


def convert_risk(r):
    if r == 1:
        return 'HIGH'
    elif r == 2:
        return 'MEDIUM'
    elif r == 3:
        return 'LOW'
    else:
        return 'ERROR'


if __name__ == '__main__':
    main()