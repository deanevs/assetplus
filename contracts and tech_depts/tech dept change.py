import pandas as pd
from pathlib import Path

# setup options
pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

# load paths and files and create dataframes
wdir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\Monthly Reports\new downloads')
mth = pd.read_csv((wdir / 'monthly_pm_status.csv'))
mth.collected = pd.to_datetime(mth.collected)
grp = mth.groupby('collected')
keys = list(grp.groups.keys())
keys.sort(reverse=True)

last_mth = mth.loc[mth.collected == keys[0]]
print(last_mth.head())
print(last_mth.shape)

# print(mth.loc[mth.n_imma == '501495'])

datadir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20221221 - bulk contracts and tech depts for billing tracker')
df = pd.read_excel((datadir / 'AP Updates.xlsx'))
df.drop(columns=['Equip Number', 'Equip Number.1', 'Serial', 'Manufacturer', 'Model', 'Asset Name', 'Risk', 'Med Dept', 'Site Name', 'Install Date', 'Division'], inplace=True)
df['Assetplus ID'] = df['Assetplus ID'].astype(str)

print(df.head())
print(df.shape)

merged = pd.merge(df, last_mth, how='inner', left_on='Assetplus ID', right_on='n_imma')
print(merged.head())
print(merged.shape)

notin = df['Assetplus ID'][~df['Assetplus ID'].isin(last_mth.n_imma)].tolist()
print(notin)


def update_lk_asset_td(data):
    return f"UPDATE LK_ASSET_TD SET FK_TD = '{data[1].upper()}' WHERE FK_ASSET = '{data[0].upper()}';\n"


def update_b_eq1996(data):
    return f"UPDATE B_EQ1996 SET UNIT_ST = '{data[1].upper()}' WHERE N_IMMA = '{data[0].upper()}';\n"


with open((datadir / 'output.txt'), 'w') as fd:
    for idx, row in merged.iterrows():
        asset = row.n_imma
        td = row['New Tech Department']
        data = (asset, td)

        fd.write(update_b_eq1996(data))
        fd.write(update_lk_asset_td(data))
        print(update_b_eq1996(data))
        print(update_lk_asset_td(data))

