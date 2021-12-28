import pandas as pd
from pathlib import Path
import sys

pd.set_option('max_columns', None)  # displays all columns
pd.set_option("max_rows", None)     # displays all rows ... change None to 100 ow whatever number
pd.set_option('display.width', 1000)

data_folder = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\PM Compliance")

kush_file = data_folder / "Compliance KPI 16_12_21.xlsx"   #"MODEL - GMDN INVESTIGATION.xlsx"
dean_file = data_folder / "20211217 - pm all assets.xls"
# kush_file = data_folder / "Compliance KPI 29_10_21 plus Pm Schedule.xlsx"
# dean_file = data_folder / "20211103 - pm all assets.xlsx"



def main():
    # create Dataframe from Kush report
    df_kush = pd.read_excel(kush_file, index_col=False, sheet_name='Asset Data')
    # print(list(df_kush.columns.values))

    # remove unwanted columns
    # cols_drop = ['CONTRACT INFO','EQUIPMENT NO','SERIAL NO','GE System No','RISK','MANUFACTURER','ASSET MODEL TYPE',
                 # 'GMDN','CONTRACT NO','Next PM Year','Next PM Month','SITE NUMBER','DEPARTMENT NAME','DIVISION']
    cols_drop = ['CONTRACT INFO','EQUIPMENT NO','SERIAL NO','GE System No','RISK','MANUFACTURER','ASSET MODEL TYPE',
                 'GMDN','CONTRACT NO','SITE NUMBER','DEPARTMENT NAME','DIVISION']
    df_kush.drop(columns=cols_drop, inplace=True)

    # rename to recognise and simplicity
    df_kush.rename(columns={'Date of last preventive work order': 'K-Last PM','INSTALLATION DATE':'K-Install',
                            'NEXT PM':'K-Next PM','STATUS':'K-Status','TECHNICAL DEPARTMENT':'Tech Dept'}, inplace=True)

    # normalise PM status
    df_kush['K-Status'].replace('In Date','IN DATE',inplace=True)
    df_kush['K-Status'].replace('Late','OUT OF DATE',inplace=True)

    # now do assetplus calc
    df_ap = pd.read_excel(dean_file, index_col=False, sheet_name='A')
    # print(list(df_ap.columns.values))

    df_ap['Date of next PM'] = pd.to_datetime(df_ap['Date of next PM'], format='%Y%m%d')
    df_ap.drop(columns=['Name','Manufacturer of part','Model Type of the part','Technical department','Risk (Asset)',
                        'Contract no.','Site no.','Med Dept','Activity Pole name'],inplace=True)

    df_ap.rename(columns={'Asset no.':'Asset ID','Date of last preventive work order':'Last PM',
                          'Date of next PM':'Next PM'},inplace=True)

    # merge the 2 dfs on asset id
    df_merge = df_kush.merge(df_ap, how='left', left_on='ASSET NO', right_on='Asset ID')
    # df_merge.drop(columns=['ASSET NO'], inplace=True)

    df = df_merge[~(df_merge['K-Status'] == df_merge['PM Status'])]

    df = df[['ASSET NO','Tech Dept','K-Install','K-Next PM','K-Status','PM Status','Asset ID','Last PM','Next PM']]
    print(df)
    print(df.info())



    from datetime import datetime

    save_file = str(data_folder) + "/" + "pm_check_" + str(datetime.today().date()) + ".xlsx"
    df.to_excel(save_file)
    print("Saved to {}".format(save_file))


if __name__ == '__main__':
    main()

"""
    cols_ap = [
        'Name',
        'Manufacturer of part',
        'Model Type of the part',
        'Technical department',
        'Risk (Asset)',
        'Contract no.',
        'Date of last preventive work order',
        'Date of next PM',
        'PM Status',
        'Site no.',
        'Med Dept',
        'Activity Pole name'
    ]

    cols_ge = ['STATUS',
        'CONTRACT INFO',
        'ASSET NO',
        'EQUIPMENT NO',
        'SERIAL NO',
        'GE System No',
        'RISK',
        'MANUFACTURER',
        'ASSET MODEL TYPE',
        'GMDN',
        'INSTALLATION DATE',
        'NEXT PM',
        'TECHNICAL DEPARTMENT',
        'CONTRACT NO',
        'Next PM Year',
        'Next PM Month',
        'SITE NUMBER',
        'DEPARTMENT NAME',
        'DIVISION'
    ]
"""