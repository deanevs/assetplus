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
lung = 'Copy of Lung Function.xlsx'

pd.set_option('max_columns', None)  # displays all columns
pd.set_option("max_rows", None)     # displays all rows ... change None to 100 ow whatever number
pd.set_option('display.width', 1000)

def main():
    df_all = pd.read_csv(main_dir / ap_ib, low_memory=False)
    df_all['FILLER1'] = df_all['FILLER1'].astype(str)

    df_lung = pd.read_excel(main_dir / lung, sheet_name='Active assets all sites')
    df_lung = df_lung[df_lung['Equipment No.'].notna()]


    for idx, row in df_all.iterrows():
        if isinstance(row['FILLER1'], float):
            df_all.at[idx, 'FILLER1'] = str(int(row['FILLER1']))

    #print(df_all[['FILLER1']].head(20))


    for idx, row in df_lung.iterrows():
        eqno = row['Equipment No.']

        if isinstance(eqno, float):
            #print(eqno)
            #print(type(eqno))
            new = str(int(eqno))
            #print(new)
            df_lung.at[idx, 'EQUIP'] = new

    # print(df_lung.head(20))
    #
    # print(df_lung.info())

    found = df_lung[df_lung['EQUIP'].isin(df_all['FILLER1'])]
    for idx, row in found.iterrows():
        sql = f"UPDATE B_EQ1996 SET N_EF = '{'LUNG'}' WHERE FILLER1 = '{row['EQUIP']}'"
        print(sql)

    # print(found)
    not_found = df_lung[~df_lung['EQUIP'].isin(df_all['FILLER1'])]
    # not_found.to_excel("not_found.xlsx", index=False)




    # print(f"Number found is {len(found)} out of {count} equipment no.")
    # not_found = df_lung[~df_lung['Equipment No.'].isin(df_all['FILLER1'])]


    # print("********************************************")
    # print(found)
    # print("********************************************")
    # print(not_found)
    # print("********************************************")

    # now do FG
    # merged = df_all.merge(found,how='inner',left_on='FILLER1', right_on='Equipment No.')
    # fg_set = merged[merged['N_EF'] == 'LUNG']
    # print(F"Out of the {len(found)} from the found in the main IB, {len(fg_set)} have the FG set")

def check_length(eq):
    return len(eq) > 1


if __name__ == '__main__':
    main()