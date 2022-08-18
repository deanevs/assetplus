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
output_filename = 'merged_' + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + '.xlsx'


def main():
    df_kat = pd.read_excel(file_path / kat_file)
    df_kat['last known PM date'].fillna('', inplace=True)
    print(f"Length of Kat file = {len(df_kat)}")

    df_nuv = pd.read_excel(file_path / nuvolo_file)
    df_nuv = df_nuv[df_nuv['Technical Department'] == 'GE Biomed']
    print(f"Length of Nuvolo = {len(df_nuv)}")

    reasons = ['new to contract','New to contract', 'CNL']

    for idx, row in df_kat.iterrows():
        last_dt = row['last known PM date']
        if len(last_dt) > 1 and last_dt not in reasons:
            try:
                df_kat.at[idx, 'LAST PM DATE'] = datetime.datetime.strptime(last_dt, '%b %Y').date()
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
        if isinstance(nuv_last_pm, pd.Timestamp) and isinstance(kat_last_pm, datetime.date):
            # print(nuv_last_pm, kat_last_pm)
            merged.at[idx, 'DELTA'] = (nuv_last_pm.date() - kat_last_pm).days


    output = file_path / output_filename
    merged.to_excel(output, index_label=False)

    print(merged.info())


if __name__ == '__main__':
    main()