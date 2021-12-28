import pandas as pd
from collections import defaultdict
import re
import numpy as np

excel = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\GMDN\\Pulse_result1.xlsx"
excel = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\GMDN\\Ultrasonic_GE_2020-06-04.xlsx"

df = pd.read_excel(excel)

gmdn = set()
manufacturer = set()

# model, manufacturer, gmdn_id, name_2,
sql = "INSERT INTO TYPES (TP_TYPE, MARQUE, CNEH_TYPE, NOM2, ASSET_PART_TYPE, REMP_PRIX) VALUES "

ultrasound_map = {
    'gmdn_name':'GMDN Preferred Term',
    'gmdn_id':'GMDN_CODE',
    'prim_di':'Primary DI',
    'manufacturer':'Company',
    'brand':'Brand',
    'model':'Version',
    'desc':'Description'
    }

p = re.compile('(?![ -~]).')

# df['Description'] = df['Description'].fillna('Blank')
# df['Brand'] = df['Brand'].fillna('Blank')
df = df.fillna('blank field')

def format_cell(din):
    in_str = str(din)
    in_str = in_str.replace("'","")
    in_str = p.sub('', in_str)
    return in_str


added = []
skipped = []
counter = 0
for index, row in df.iterrows():
    counter += 1

    gmdn_name = format(row[ultrasound_map['gmdn_name']].upper())
    gmdn_id = format(row[ultrasound_map['gmdn_id']])
    prim_di = format(row[ultrasound_map['prim_di']])
    manufacturer = format(row[ultrasound_map['manufacturer']].upper()[:50])
    brand = format(row['Brand'].upper())
    model = format(row[ultrasound_map['model']].upper())
    desc = format(row[ultrasound_map['Description']].upper())

    # concat fields for more details
    name_2 = "Primary DI: {}\nBrand: {}\nDecsription: {}".format(prim_di, brand, desc)[:1024]

    ap_key = (model, manufacturer)
    if ap_key not in added:
        added.append(ap_key)
        model_data = (model, manufacturer, gmdn_id, name_2, 1, 1)
        print(model_data)
        # if counter > 2999 and counter < 4000:
        #     sql = sql + str(model_data) + ',\n'
    else:
        skipped.append(ap_key)


# now create sql query
# sql = "INSERT INTO EQ_CNEH ('N_NOM_CNEH','NOM') VALUES "
# for item in gmdn:
#     sql = sql + str(item) + ',\n'

# sql_man = "INSERT INTO MARQUES (MA_NOM) VALUES "
# for man in manufacturer:
#     sql_man = sql_man + man + ',\n'



# print(sql)
print(*skipped, sep='\n')
