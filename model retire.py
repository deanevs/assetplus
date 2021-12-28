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
    start_time = time.time()

    # set active directory path
    active_dir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20210722 - Retire Models')

    # get files
    active_assets = active_dir / 'ALL ACTIVE - 23-07-21.xls'
    active_models = active_dir / 'models-active.xlsx'


    # get dataframes
    df_active_assets = pd.read_excel(active_assets, index_col=False, sheet_name='A')
    df_active_models = pd.read_excel(active_models, index_col=False)

    active_man_models_list = set()
    active_model_list = set()

    # make a Set tuple of manufacturer, model from the all active assets extract
    for index, row in df_active_assets.iterrows():
        manufacturer = convert_str(row['Manufacturer'])
        model_raw = row['Model Type']
        try:
            model = convert_str(model_raw)
        except:
            # print('assets')
            # print(manufacturer)
            # print(model_raw)
            model = 'error'
            print(model)


        # key = (manufacturer, model)
        key = manufacturer + ' - ' + model
        active_man_models_list.add(key)


    # now
    not_matched = 0
    matched = 0

    for idx2, row2 in df_active_models.iterrows():
        model_lup = convert_str(row2['Type'])
        manufacturer_lup = convert_str(row2['Manufacturer'])


        # key2 = (manufacturer_lup, model_lup)
        key2 = manufacturer_lup + ' - ' + model_lup

        active_model_list.add(key2)


        if key2 not in active_man_models_list:
            print(key2)
            not_matched += 1
        else:
            matched += 1

    print(f"Active Models Official = {len(active_model_list)}")
    print(f"Unique from Active Assets Export = {len(active_man_models_list)}")
    print(f"Not Matched Total {not_matched}")
    print(f"Matched = {matched}")
    # df_analysis.to_excel(get_datetime() + "_analysis.xlsx", index=False)
    print("Time taken: {}".format(str(time.time() - start_time)))




def convert_str(inp):
    if isinstance(inp, str):
        #print(inp)
        return inp
    elif pd.isna(inp):
        print(f"isna{inp}")
        return ''
    elif isinstance(inp, float):
        print(f"Float {inp}")
        return int(str(inp))
    elif isinstance(inp, int):
        print(f"Interger {inp}")
        return str(inp)



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