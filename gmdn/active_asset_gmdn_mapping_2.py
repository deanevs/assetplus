import pandas as pd
from pathlib import Path
import numpy as np
import datetime
import sys
import time
import math

# setup options
pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

def main():
    # set start time
    start_time= time.time()

    # set active directory path
    active_dir = Path(r'C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN')
    dir2 = Path(r'C:\Users\212628255\Workspace\PyCharmProjects')

    # get all files of interest
    active_gmdn = active_dir / 'active_gmdn_terms.xlsx'
    results = dir2 / '2020-07-06 17-06-09_analysis.xlsx'

    # create associated dataframes
    df_active_gmdn = pd.read_excel(active_gmdn, index_col=False)
    df_result = pd.read_excel(results, index_col=False)

    # reset index to gmdn code for faster lookup
    if df_active_gmdn['GMDN_CODE'].is_unique:
        df_active_gmdn = df_active_gmdn.set_index('GMDN_CODE')

    # if gmdn_code been filled in then
    for index, row in df_result.iterrows():
        if not isinstance(row['NEW_TERM_1'], str):
            if isinstance(row['NEW_CODE'], str): # is not None or not math.isnan(row['NEW_CODE']):
                code = str(int(row['NEW_CODE']))
            else:
                try:
                    code = str(int(row['GMDN']))
                except ValueError:
                    print("Value Error for {}".format(code))
                    continue
            # now lookup index in active gmdn
            terms = get_gmdn_terms(df_active_gmdn, code)

            if terms is not None:
                #print("Adding {}\n{}\n{}".format(terms[0], terms[1], terms[2]))
                df_result.loc[index, 'NEW_CODE'] = code
                df_result.loc[index, 'NEW_TERM_1'] = terms[0]
                df_result.loc[index, 'NEW_TERM_2'] = terms[1]
                df_result.loc[index, 'STATUS'] = terms[2]

        else:
            print("Skipping {}".format(str(int(row['NEW_CODE']))))

    #for idx, row in df_result.iterrows():
        # if row.STATUS == 'Active':
        #     print(row)

    df_result.to_excel(get_datetime() + "_analysis.xlsx", index=False)
    print("Time taken: {}".format(str(time.time() - start_time)))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_gmdn_terms(df, code):
    try:
        new_term_1 = df.loc[int(code)][0]
        new_term_2 = df.loc[int(code)][1]
        status = df.loc[int(code)][2]
        return (new_term_1, new_term_2, status)
    except KeyError:
        print("No index for {}".format(code))
        return(None)


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