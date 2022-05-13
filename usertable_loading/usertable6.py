

import pandas as pd
from pathlib import Path

# setup display options for debugging
pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)

filedir = Path(r"C:\Users\212628255\Documents\2 GE\AssetPlus\Projects\Usertable Loading")
filename = "Copy of Contacts so far.xlsx"

df = pd.read_excel(filedir / filename,'Sheet1')

contact_dict = {
    'Alvi Ajdini':9,
    'Jonathan Harper':10,
    'Nahila Iqbal':11,
    'Luis Alves':12,
    'David Tao':13,
    'Lawrence Paralejas':14,
    'Shirley Featherston':15,
    'Sophie Peregrine':16,
    'Sally Kirkaldy':17,
    'Uyen Attrill':18,
    'Kannah Vasishtan':19,
    'Alan Glover':21,
    'Susie Wickes':22,
    'Jakson Rounding':23,
    'Mark Bartholomew':24,
    'Bernadette Tucker':25,
    'Janine Boucher':26,
    'Matthew Buck':27
}


for idx, row in df.iterrows():
    asset_id = row['AP Identifier']
    contact = row['Main Contact']
    sql = f"UPDATE B_EQ1996 SET ID_USERTABLE6={contact_dict[contact]} WHERE N_IMMA = '{asset_id}'"
    print(sql)