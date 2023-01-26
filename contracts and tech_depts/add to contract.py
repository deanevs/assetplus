"""
Updates tech dept and adds to contract
Currently done separately for tech depts and then seperately for each contract since the type is different.
"""

import pandas as pd
from pathlib import Path
import sys

# setup options
pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

# load paths and files and create dataframes
wdir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\Monthly Reports\new downloads')
datadir = Path(r'C:\Users\212628255\Documents\2 GE\AssetPlus\7 Projects\20221221 - bulk contracts and tech depts for billing tracker')


# use the monthly capture and get the last month data for compare
mth = pd.read_csv((wdir / 'monthly_pm_status.csv'))
mth.collected = pd.to_datetime(mth.collected)
grp = mth.groupby('collected')
keys = list(grp.groups.keys())
keys.sort(reverse=True)

last_mth = mth.loc[mth.collected == keys[0]]
print(last_mth.head())
print(last_mth.shape)

# print(mth.loc[mth.n_imma == '501495'])

# setup the requested updates data
df = pd.read_excel((datadir / 'AP Updates.xlsx'))
df.drop(columns=['Equip Number', 'Equip Number.1', 'Serial', 'Manufacturer', 'Model', 'Asset Name', 'Risk', 'Med Dept', 'Site Name', 'Install Date', 'Division'], inplace=True)
df['Assetplus ID'] = df['Assetplus ID'].astype(str)
print(df.head())
print(df.shape)

# merge to get column differences - using inner join should get same number as df, if not it is the ones
# that have added/removed since
merged = pd.merge(df, last_mth, how='inner', left_on='Assetplus ID', right_on='n_imma')
print(merged.head())
print(merged.shape)

# use this to find the missing ones
# notin = df['Assetplus ID'][~df['Assetplus ID'].isin(last_mth.n_imma)].tolist()
# print(notin)

# method is to emulate AP by copying for each PM plan, hence create separate data for each
pm_only = merged.loc[merged['New Contract'] == 'MMS PM ONLY 20-25']
print(pm_only.head(10))
print(pm_only.shape)

fully_comp = merged.loc[merged['New Contract'] == 'MMS FULLY COMP 20-25']
print(fully_comp.head(10))
print(fully_comp.shape)

def insert_hist_eq(contract, asset, cont_type, fin_period_from='20220331', today='20221221'):
    """ This should be the same for both PM ONLY and FULLY COMP except for the pm type field
        Note the med dept and location are set to NULL since this would require a lookup """
    sql = f"INSERT INTO HISTO_EQ (N_CONTRAT,CODE_TYPE,N_IMMA,ANNEE_EXO,DATE_EFFET,DATE_ECHU,PRORATA,TTC_ANNEE,HT_NET," \
          f"TTC_NET,TTC_PREV,TTC_CORR,VAC_HT,FRE_MP,NB_VCM,PD_MP,PD_MC,PD_SEUIL,NB_AR_BL,DMCD_B,DMI,T_MI,DEFAUT,COMMENTAIRE," \
          f"PARA1,GENERIC,GENERIC_SEQ,FK_LIEU_N_LIEU,FK_UNITES_N_UF,FK_BUDGET_NU_COMPTE,FK_BUDGET_AN_EXO," \
          f"FINANCIAL_PERIOD_FROM,FINANCIAL_PERIOD_TO,INACTIVE_CONTRACT_ASSET_DATE,NB_VCQ,PD_MP_INT,PD_MC_INT," \
          f"ASSET_ANNUAL_COST,ASSET_ANNUAL_NET_COST,YEAR_PERIOD_FROM,YEAR_PERIOD_TO,TAXE_CODE,TAXE_RATE,ASSET_ANNUAL_PRICE_HT," \
          f"ASSET_ANNUAL_PRICE_TTC,ASSET_ANNUAL_PRICE_NET,ASSET_ANNUAL_COST_HT,ASSET_ANNUAL_COST_TTC,ASSET_ANNUAL_COST_NET," \
          f"PREVIOUS_TAXE_RATE,PREVIOUS_DISCOUNT_RATE,PREVIOUS_PRORATA,CURRENT_PRORATA,PREV_ASSET_ANNUAL_PRICE_HT," \
          f"PREV_ASSET_ANNUAL_COST_HT,IS_FIXE_PRICE_COST_USED) " \
          f"VALUES (" \
          f"'{contract}','{cont_type}','{asset}',2022,'20220331','20230330',1,0,0,0,1,0,NULL,NULL,NULL,NULL,NULL,0,NULL,0,0," \
          f"NULL,'2',NULL,'{today}','0',0,NULL,NULL,NULL,NULL,'{fin_period_from}','20230330',NULL,NULL,0,0,0,0,'20220331'," \
          f"'20230330',NULL,0,0,0,0,0,0,0,0,0,0,0,0,0,0);\n"
    return sql

def update_b_eq1996(contract, asset):
    sql = f"UPDATE B_EQ1996 SET N_MARCHE ='{contract}',VAC_HT =NULL,FRE_MP =NULL,PD_MP =NULL,NB_VCM =NULL," \
          f"DMCD_B =0,PD_MC =NULL,PD_SEUIL =0,NB_AR_BL =NULL,DMI =0,T_IM =NULL,NB_VCQ =NULL,PD_MC_INT =0,PD_MP_INT =0," \
          f"P_M_PRIX_N =0,P_M_TEMPOR =1 " \
          f"WHERE N_IMMA ='{asset}';\n"
    return sql


# cnt = 0
with open((datadir / 'fully_comp.txt'), 'w') as fd:
    for idx, row in fully_comp.iterrows():
        # cnt += 1
        # if cnt <= 10:
        #     continue
        asset = row.n_imma
        contract = row['New Contract']
        insert = insert_hist_eq(contract, asset, 'COMP')
        fd.write(insert)
        update = update_b_eq1996(contract, asset)
        fd.write(update)
        fd.write('GO\n')


# cnt = 0
with open((datadir / 'pm_only.txt'), 'w') as fd:
    for idx, row in pm_only.iterrows():
        # cnt += 1
        # if cnt <= 10:
        #     continue
        asset = row.n_imma
        contract = row['New Contract']
        insert = insert_hist_eq(contract, asset, 'SM')
        fd.write(insert)
        update = update_b_eq1996(contract, asset)
        fd.write(update)
        fd.write('GO\n')



