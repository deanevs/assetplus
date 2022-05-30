import pandas as pd
from pathlib import Path
import datetime
import sys

pd.set_option('max_columns', None)  # displays all columns
pd.set_option("max_rows", None)     # displays all rows ... change None to 100 ow whatever number
pd.set_option('display.width', 1000)

file_path = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\Nuvolo\Projects\20220517 - Compare files for Kat")
nuvolo_file = "x_nuvo_eam_clinical_devices.xlsx"
kat_file = 'GEMVS 23_05_22.xlsx'
output = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\3 Sites\2 Spire\Nuvolo\output")


def main():
    df_kat = pd.read_excel(file_path / kat_file)
    df_kat['last known PM date'].fillna('', inplace=True)
    print(f"Length of Kat file = {len(df_kat)}")

    df_nuv = pd.read_excel(file_path / nuvolo_file)
    df_nuv = df_nuv[df_nuv['Technical Department'] == 'GE Biomed']
    print(f"Length of Nuvolo = {len(df_nuv)}")

    # before merge, clean up columns
    # convert string May 2020 to a date

    # df_kat['last known PM date'] = df_kat.apply(
    #     lambda x: x['last known PM date'].replace(' ', '-'), axis=1
    # )
    reasons = ['new to contract','New to contract', 'CNL']
    for idx, row in df_kat.iterrows():
        last_dt = row['last known PM date']
        if len(last_dt) > 1 and last_dt not in reasons:
            #dts = last_dt.replace(' ', '-')
            try:
                dt = datetime.datetime.strptime(last_dt, '%b %Y').date() # .strftime('%d-%m-%Y')
                df_kat.at[idx, 'LAST PM DATE'] = dt

            except:
                print(f"*************************************ERROR - {last_dt}")
        else:
            df_kat.at[idx, 'LAST PM DATE'] = ''


    merged = df_nuv.merge(df_kat, how='outer', left_on='Asset Tag', right_on='New asset tag')
    print(f"Length of Merged = {len(merged)}")



    # now compare last pm dates

    for idx, row in merged.iterrows():
        nuv_last_pm = row['Last Service Date']
        kat_last_pm = row['LAST PM DATE']
        # print(type(nuv_last_pm))
        print(type(kat_last_pm))

        if isinstance(nuv_last_pm, pd.Timestamp) and isinstance(kat_last_pm, datetime.date):
            print(nuv_last_pm, kat_last_pm)
            # nuv_dt = nuv_last_pm.date()
            # merged.at[idx,'NUVOLO_LAST_PM_DATE'] = nuv_dt
            # kat_dt = datetime.datetime.strptime(kat_last_pm, '%d-%m-%Y').date()
            # print(nuv_dt, kat_dt)
            delta = (nuv_last_pm.date() - kat_last_pm).days
            merged.at[idx, 'DELTA'] = (nuv_last_pm.date() - kat_last_pm).days

    output = file_path / "merged6.xlsx"
    merged.to_excel(output, index_label=False)

    print(merged.info())
    # print(merged)












if __name__ == '__main__':
    main()