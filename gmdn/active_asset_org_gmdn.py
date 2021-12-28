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


def convert_str(inp):
    if isinstance(str, inp):
        gmdn = None
    elif isinstance(float, inp):
        gmdn = str(int(inp))
    else:
        gmdn = None
    return gmdn

def main():
    # set start time
    start_time = time.time()

    # set active directory path
    active_dir = Path(r'C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN')

    # get files
    active_assets = active_dir / 'active_assets_20_08_20.xls'
    active_gmdn = active_dir / 'active_gmdn_terms.xlsx'
    prev_lup = active_dir / '2020-07-08 08-11-16_analysis.xlsx'

    # get dataframes
    df_active_assets = pd.read_excel(active_assets, index_col=False, sheet_name='A')
    # df_gmdn = pd.read_excel(active_gmdn, index_col=False)
    df_lup = pd.read_excel(prev_lup, index_col=False)

    # copy active assets and add 3 columns for new dataframe
    # add_cols = ['NEW_CODE']
    # df_analysis = pd.concat([df_active_assets, pd.DataFrame(columns=add_cols)])

    # reset index for faster lookup
    # df_lup = df_lup.set_index(['Asset Plus Identifier'])

    not_found = []

    for index, row in df_active_assets.iterrows():
        asset = row['Asset Plus Identifier']
        found = False

        for idx2, row2 in df_lup.iterrows():
            asset_lup = row2['Asset Plus Identifier']
            if asset == asset_lup:
                found = True
                break

        if found == False:
            print(asset)
            not_found.append(asset)

    print("Number not found is {}".format(str(len(not_found))))
    print(s for s in not_found)


        # if ng == 'y' or ng == 'u':
        #     ap_code = str(row['AP code'])
        #     try:
        #         new_code = str(int(row['GMDN_CODE']))
        #         #print(new_code)
        #     except:
        #         print("EMPTY for {}".format(str(index)))
        #         continue
        #
        #     # now lookup index in active gmdn
        #     try:
        #         new_term_1 = df_gmdn.loc[int(new_code)][0]
        #         new_term_2 = df_gmdn.loc[int(new_code)][1]
        #     except KeyError:
        #         print("No index for {}".format(new_code))
        #         continue
        #
        #     for idx2, row2 in df_analysis.iterrows():
        #         if str(row2['GMDN']) == ap_code:
        #             row2['NEW_CODE'] = new_code,
        #             row2['NEW_TERM_1'] = new_term_1,
        #             row2['NEW_TERM_2'] = new_term_2


    # df_analysis.to_excel(get_datetime() + "_analysis.xlsx", index=False)
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