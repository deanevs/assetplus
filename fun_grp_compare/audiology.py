import pandas as pd
import numpy as np
from pathlib import Path

main_dir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\1 Projects\20220625 - Aheed Functional Groups')
ap_ib = '20220704 - ALL ASSETS.csv'
audiology = 'audiology-Finalised Asset List.xlsx'
sleep = 'sleep-Export-18-09-2020.xls'
cardiac = 'Copy of CE reviewed 2020.08.26 Cardiac ECHO HH.xlsx'
echo = 'Copy of Cardiac Echo SMH - Finalised.xlsx'
vascular = 'Up to date Vascular list 12-11-2020.xlsx'

pd.set_option('max_columns', None)  # displays all columns
pd.set_option("max_rows", None)     # displays all rows ... change None to 100 ow whatever number
pd.set_option('display.width', 1000)

def main():
    df_all = pd.read_csv(main_dir / ap_ib, low_memory=False)
    #print(df_all.head())


    df_all['FILLER1'] = df_all['FILLER1'].astype(str)
    #print(df_all.info())

    # for fg in [audiology, sleep, cardiac, echo, vascular]:
    #    df = pd.read_excel(main_dir / fg)

    df_audiology = pd.read_excel(main_dir / audiology, sheet_name='Sheet1')
    #print(df_audiology.head())
    df_audiology['Equipment No.'] = df_audiology['Equipment No.'].astype(str)
    #print(df_audiology.info())

    found = df_audiology[df_audiology['Equipment No.'].isin(df_all['FILLER1'])]

    print(f"Number found is {len(found)} out of {len(df_audiology)} in the audiology file")
    not_found = df_audiology[~df_audiology['Equipment No.'].isin(df_all['FILLER1'])]

    # print("********************************************")
    # print(found)
    # print("********************************************")
    # print(not_found)
    # print("********************************************")

    # now do FG
    merged = df_all.merge(found,how='inner',left_on='FILLER1', right_on='Equipment No.')
    fg_set = merged[merged['N_EF'] == 'AUDIOLOGY']
    print(F"Out of the {len(found)} from the found in the main IB, {len(fg_set)} have the FG set")




if __name__ == '__main__':
    main()