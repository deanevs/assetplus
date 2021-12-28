import pandas as pd
from pathlib import Path
import numpy as np
import datetime
import sys
import time

# setup options
pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

def main():
    # set start time
    start_time= time.time()

    # set active directory path
    active_dir = Path(r'C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN')

    # get all files of interest
    active_assets = active_dir / 'active_assets_30_06_20.xls'
    active_gmdn = active_dir / 'active_gmdn_terms.xlsx'
    partial_map = active_dir / 'gmdn_result2.xlsx'

    # create associated dataframes
    df_active_assets = pd.read_excel(active_assets, index_col=False, sheet_name='A')
    df_active_gmdn = pd.read_excel(active_gmdn, index_col=False)
    df_partial_map = pd.read_excel(partial_map, index_col=False, sheet_name='GMDN Terms')

    # copy active assets and add 3 columns for new dataframe
    add = ['NEW_CODE', 'NEW_TERM_1', 'NEW_TERM_2']
    df_analysis = pd.concat([df_active_assets, pd.DataFrame(columns=add)])

    # reset index to gmdn code for faster lookup
    if df_active_gmdn['GMDN_CODE'].is_unique:
        df_active_gmdn = df_active_gmdn.set_index('GMDN_CODE')

    # if gmdn_code been filled in then
    #
    for index, row in df_partial_map.iterrows():
        ng = row['NG']
        if ng == 'y' or ng == 'u':
            ap_code = str(row['AP code'])
            try:
                new_code = str(int(row['GMDN_CODE']))
                #print(new_code)
            except:
                print("EMPTY for {}".format(str(index)))
                continue

            # now lookup index in active gmdn
            try:
                new_term_1 = df_active_gmdn.loc[int(new_code)][0]
                new_term_2 = df_active_gmdn.loc[int(new_code)][1]
            except KeyError:
                print("No index for {}".format(new_code))
                continue

            for idx2, row2 in df_analysis.iterrows():
                if str(row2['GMDN']) == ap_code:
                    row2['NEW_CODE'] = new_code,
                    row2['NEW_TERM_1'] = new_term_1,
                    row2['NEW_TERM_2'] = new_term_2


    df_analysis.to_excel(get_datetime() + "_analysis.xlsx", index=False)
    print("Time taken: {}".format(str(time.time() - start_time)))


def get_datetime():
    """
    Useful for setting unique filename when testing
    Arguments = Nothing
    Returns output 2017-01-09 09:35:15
    """
    curr_datetime = datetime.datetime.now()
    new_time = curr_datetime.strftime("%Y-%m-%d %H-%M-%S")
    return new_time

if __name__ == '__main__':
    main()