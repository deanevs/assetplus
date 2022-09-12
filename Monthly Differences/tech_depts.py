

import datetime
import pandas as pd
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import sys

pd.options.display.max_columns = None
pd.options.display.max_rows= None     # displays all rows ... change None to 100 ow whatever number
pd.options.display.width = 1000

# controls
do_excel = True

# how many months to display from most recent
NUM_MONTHS = 2


wdire = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\Monthly Differences')
output = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\Monthly Differences\Tech Depts')
assets = pd.read_csv((wdire / 'INFOASSETSRETIREDAFTER2015.csv')) #, parse_dates=True)
mth = pd.read_csv((wdire / 'monthly-pm-status.csv')) #,parse_dates=True)

mth.collected = pd.to_datetime(mth.collected)
grp = mth.groupby('collected')
keys = list(grp.groups.keys())
keys.sort(reverse=True)

# stores dict values from each month to create dataframe
rows_list = []

def column_widths(df, sheet_name, writer):
    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets[sheet_name].set_column(col_idx, col_idx, column_width + 8)

assets = assets[['N_IMMA', 'FILLER1', 'N_NOM_CNEH', 'NOM', 'MARQUE', 'TYP_MOD', 'MES1', 'UNIT_ST', 'N_MARCHE']]
assets = assets.rename(columns={'N_IMMA': 'ASSETPLUS_ID',
                                'FILLER1': 'EQUIP_NO',
                                'N_NOM_CNEH': 'GMDN',
                                'NOM': 'NAME',
                                'MARQUE': 'MANUFACTURER',
                                'TYP_MOD': 'MODEL',
                                'MES1': 'INSTALL_DATE',
                                'UNIT_ST': 'TECH_DEPT',
                                'N_MARCHE': 'CONTRACT_NO'
                                })

# iterate through each month
for x in range(len(keys) - 1):
    if x < NUM_MONTHS:
        # set up month and last_month dfs
        df_last = mth.loc[mth.collected == keys[x]]
        df_lastlast = mth.loc[mth.collected == keys[x + 1]]

        # outer join allows detection of new and retired assets
        outer = pd.merge(df_last, df_lastlast, how='outer', on='n_imma')
        print(f"Outer join length {len(outer)}")

        # inner join allows detection of changes from month to month
        inner = pd.merge(df_last, df_lastlast, how='inner', on='n_imma')
        print(f"Inner join length {len(inner)}")

        # get active fields for both months
        delta_td = inner[inner.apply(lambda x: x['tech_dept_x'] != x['tech_dept_y'], axis=1)]

        delta_td = delta_td.drop(columns=[ 'contrac_x', 'status_std_x', 'status_cnl_x', 'contrac_y', 'status_std_y', 'status_cnl_y'],axis=1)

        delta_td = pd.merge(delta_td, assets, how='left', left_on='n_imma', right_on='ASSETPLUS_ID')

        delta_td = delta_td.drop(columns=['n_imma', 'TECH_DEPT'])

        delta_td.reset_index(drop=True, inplace=True)

        # arrange order of columns
        delta_td = delta_td[['ASSETPLUS_ID',
                                        'EQUIP_NO',
                                        'GMDN',
                                        'NAME',
                                        'MANUFACTURER',
                                        'MODEL',
                                        'INSTALL_DATE',
                                        'CONTRACT_NO',
                                        'tech_dept_y',
                                        'tech_dept_x']]
        # rename column headers
        delta_td = delta_td.rename(columns={'tech_dept_y': f'TECH_DEPT_{keys[x + 1].date()}',
                                                        'tech_dept_x': f'TECH_DEPT{keys[x].date()}'
                                                        })

        delta_td.fillna(value='', inplace=True)

        # set up excel writer
        writer = pd.ExcelWriter((output / f'tech_dept_changes_{keys[x].date()}.xlsx'), engine='xlsxwriter')

        print("**************************************************************************************************")
        print(f"CHANGES OF TECH DEPTS FOR EXISTING ASSETS {keys[x].date()}")
        print("**************************************************************************************************")
        print(delta_td)
        if do_excel:
            delta_td.to_excel(writer, sheet_name='delta', index=False)
            column_widths(delta_td, 'delta', writer)

        # *********************************** ADDED **************************************

        # create separate dataframes for added and retired
        added = outer[outer.collected_y.isna()]
        added_td = added[added.tech_dept_x.notna()]
        added_td = pd.merge(added_td, assets, how='left',
                            left_on='n_imma', right_on='ASSETPLUS_ID')
        added_td = added_td.drop(
            columns=['collected_y', 'collected_x', 'n_imma', 'tech_dept_y', 'contrac_y', 'status_std_y', 'status_cnl_y',
                     'tech_dept_x', 'contrac_x', 'status_std_x', 'status_cnl_x'])

        added_td.fillna(value='', inplace=True)

        print("**************************************************************************************************")
        print(f" NEWLY ADDED ASSETS ADDED TO TECH DEPT {keys[x].date()}")
        print("**************************************************************************************************")
        print(added_td)
        if do_excel:
            added_td.to_excel(writer, sheet_name='added', index=False)
            column_widths(added_td, 'added', writer)

        # *********************************** RETIRED **************************************
        retired = outer[outer.collected_x.isna()]
        retired_td = retired[retired.tech_dept_y.notna()]
        retired_td = pd.merge(retired_td, assets, how='left',
                              left_on='n_imma', right_on='ASSETPLUS_ID')
        retired_td.drop(
            columns=['collected_x', 'collected_y', 'n_imma', 'tech_dept_y', 'contrac_y', 'status_std_y', 'status_cnl_y',
                     'tech_dept_x', 'contrac_x', 'status_std_x', 'status_cnl_x'], inplace=True)

        retired_td.fillna(value='', inplace=True)

        print("**************************************************************************************************")
        print(f"RETIRED ASSETS REMOVED FROM TECH DEPT {keys[x].date()}")
        print("**************************************************************************************************")
        print(retired_td)
        if do_excel:
            retired_td.to_excel(writer, sheet_name='retired', index=False)
            column_widths(retired_td, 'retired', writer)

        writer.save()
        print("\n****************************************************************************************************************************************************************************************************\n`")