import pandas as pd
import numpy as np
from collections import defaultdict
import sys


def main():
    # fn = 'C:\\Users\\212628255\\Documents\\GE\AssetPlus\\7 Projects\\New Database\\SPIRE PYTHON TEMPLATE FILE.xlsx'
    fn = 'C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\Spire IB\\PREV_EQP_15_09.xlsx'
    # create dataframe
    df = pd.read_excel(fn) #, sheet_name='PREV_MAINT')
    print(df.shape)

    # ignore retired PM
    df = df[df['DATE_REFOR_UNIT_PM'].isnull()]
    print(df.shape)
    #
    # sys.exit()

    d_assets = defaultdict(list)


    for index, row in df.iterrows():
        asset = row['N_IMMA']
        pm = row['NU_PREVENT']
        status = str(row['STATUE'])
        retired = row['DATE_REFOR_UNIT_PM']

        d_assets[asset].append((pm,status))

    for k,v in d_assets.items():
        if len(v) > 1:
            print(k,v)

    print(str(len(d_assets.keys())))

if __name__ == '__main__':
    main()