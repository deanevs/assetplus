

import datetime
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import sys

pd.options.display.max_columns = None
pd.options.display.max_rows= None     # displays all rows ... change None to 100 ow whatever number
pd.options.display.width = 1000

# controls

do_excel = True

wdire = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20220822 - Added Retired Monthly Differences')
assets = pd.read_csv((wdire / 'INFOASSETSRETIREDAFTER2015.csv')) #, parse_dates=True)
mth = pd.read_csv((wdire / 'monthly-pm-status.csv')) #,parse_dates=True)

mth.collected = pd.to_datetime(mth.collected)
grp = mth.groupby('collected')
keys = list(grp.groups.keys())
keys.sort(reverse=True)

# how many months to display from most recent
NUM_MONTHS = 1

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
        # inner join allows detection of changes from month to month
        inner = pd.merge(df_last, df_lastlast, how='inner', on='n_imma')
        # get active fields for both months

        # do month to month changes for existing assets
        inner = inner.fillna('-------') # needed because next statement since NaN != NaN

        delta_contract = inner[inner.apply(lambda x: x['contrac_x'] != x['contrac_y'], axis=1)]
        delta_contract = delta_contract.drop(
            columns=['tech_dept_y', 'status_std_y', 'status_cnl_y', 'tech_dept_x', 'status_std_x',
                     'status_cnl_x', 'collected_x', 'collected_y'])

        delta_contract = pd.merge(delta_contract, assets, how='left', left_on='n_imma', right_on='ASSETPLUS_ID')

        delta_contract = delta_contract.drop(columns=['n_imma', 'CONTRACT_NO'])

        delta_contract.reset_index(drop=True, inplace=True)

        # arrange order of columns
        delta_contract = delta_contract[['ASSETPLUS_ID',
                                        'EQUIP_NO',
                                        'GMDN',
                                        'NAME',
                                        'MANUFACTURER',
                                        'MODEL',
                                        'INSTALL_DATE',
                                        'TECH_DEPT',
                                        'contrac_y',
                                        'contrac_x']]
        # rename column headers
        delta_contract = delta_contract.rename(columns={'contrac_y': f'CONTRACT_{keys[x + 1].date()}',
                                                        'contrac_x': f'CONTRACT_{keys[x].date()}'
                                                        })

        # set up excel writer
        writer = pd.ExcelWriter((wdire / f'contract_changes_{keys[x].date()}.xlsx'), engine='xlsxwriter')

        print("**************************************************************************************************")
        print(f"CHANGES OF CONTRACTS FOR EXISTING ASSETS {keys[x].date()}")
        print("**************************************************************************************************")
        print(delta_contract)
        if do_excel:
            delta_contract.to_excel(writer, sheet_name='delta', index=False)
            column_widths(delta_contract, 'delta', writer)

        # *********************************** ADDED **************************************

        # create separate dataframes for added and retired
        added = outer[outer.collected_y.isna()]

        added_contract = added[added.contrac_x.notna()]

        added_contract = pd.merge(added_contract, assets, how='left',
                                  left_on='n_imma', right_on='ASSETPLUS_ID')
        added_contract = added_contract.drop(
            columns=['collected_y', 'collected_x', 'n_imma', 'tech_dept_y', 'contrac_y', 'status_std_y', 'status_cnl_y',
                     'tech_dept_x', 'contrac_x', 'status_std_x', 'status_cnl_x'])

        print("**************************************************************************************************")
        print(f" NEWLY ADDED ASSETS ADDED TO CONTRACT {keys[x].date()}")
        print("**************************************************************************************************")
        print(added_contract)
        if do_excel:
            added_contract.to_excel(writer, sheet_name='added', index=False)
            column_widths(added_contract, 'added', writer)

        # *********************************** RETIRED **************************************
        retired = outer[outer.collected_x.isna()]
        retired_contract = retired[retired.contrac_y.notna()]
        retired_contract = pd.merge(retired_contract, assets, how='left',
                                    left_on='n_imma', right_on='ASSETPLUS_ID')
        retired_contract.drop(
            columns=['collected_x', 'collected_y', 'n_imma', 'tech_dept_y', 'contrac_y', 'status_std_y', 'status_cnl_y',
                     'tech_dept_x', 'contrac_x', 'status_std_x', 'status_cnl_x'], inplace=True)

        print("**************************************************************************************************")
        print(f"RETIRED ASSETS REMOVED FROM CONTRACT {keys[x].date()}")
        print("**************************************************************************************************")
        print(retired_contract)
        if do_excel:
            retired_contract.to_excel(writer, sheet_name='retired', index=False)
            column_widths(retired_contract, 'retired', writer)

        writer.save()

        print("\n***********************   *****************************************   ****************************\n")