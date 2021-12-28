import pandas as pd
import numpy as np
from pathlib import Path
from fuzzywuzzy import fuzz
from collections import defaultdict
from fuzzywuzzy import process
import operator
import sys

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

dir_path = Path(r"C:\Users\212628255\Documents\GE\AssetPlus\7 Projects\GMDN")
file_to_open1 = dir_path / "ap_gmdn.csv"
file_to_open2 = dir_path / "gmdn_code_terms.csv"

df_ap = pd.read_csv(file_to_open1)
df_gmdn = pd.read_csv(file_to_open2)



df_ap.drop(columns=['F_SPECC','F_SPECL','F_SPECL2','F_RET','EQ_AMT_COM','CRIT_AC','CRIT_ACT','NU_COMPTE','INSERT_DATE',
                    'UPDATE_DATE','RISKCODE','ECR_MODCODE','REMP_PRIX','CH1','CH2','CH3','CH4','CH5'], inplace=True)

print(df_ap.head())
print(df_gmdn.head())

choices = df_gmdn['TERM_NAME'].tolist()
d = defaultdict(list)

headers = ['AP Code', 'AP Term Name', 'GMDN Code1', 'Name1', ]
df_analysis = pd.DataFrame(columns=)

for index, row in df_ap.iterrows():
    ap_gmdn_term = row['NOM']
    ap_gmdn_code = row['N_NOM_CNEH']
    result = process.extract(ap_gmdn_term, choices, limit=3)
    d[ap_gmdn_code].append(result)
    print("{}\t{}".format(ap_gmdn_code,ap_gmdn_term))
    print(result)

for k,v in d.items():
    print(k)
    print(v)


