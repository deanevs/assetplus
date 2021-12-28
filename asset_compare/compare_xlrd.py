import openpyxl
import csv
import xlrd
from openpyxl import load_workbook

input_path = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Project Management\\New Database\\"
ap_file = input_path + "B_EQ1996_ACTIVE.csv"        # from assetplus B_EQ1996
spire_biomed = input_path + "SPIRE_BIOMED.csv"       # Lisa DB file that excludes DI assets (approx 500)
spire_imaging = input_path + "SPIRE_IMAGING.csv"

ap_dic = {}
ge_dic = {}

active_assets_ap = 0
active_assets_ge = 0

with open(ap_file, 'r', encoding='utf-8-sig') as fd:
    dr = csv.DictReader(fd)
    for row in dr:
        active_assets_ap += 1
        asset_id = row['N_IMMA'].strip()
        details = {
            "serial": row['N_SERI'],
            "manufacturer": row['MARQUE'],
            "model": row['TYP_MOD'],
            "price": row['PRIX'],
            "install": row['MES1'],
            "tech_dept": row['UNIT_ST'],
            "last_pm": row['D_DER_I_P'],
            "last_cm": row['D_DER_I_C'],
            #"department": row['NOM_UF'].strip(),
            #"site": row['N_ETAB'].strip(),
            #"div": row['POLE_NAME'].strip(),
            "ge_sys_no": row['N_PRODUIT_FOUR']
        }
        ap_dic[asset_id] = details

# for k, v in ap_dic.items():
#     print(k, v)

with open(spire_biomed, 'r', encoding='utf-8') as fd:
    dr = csv.DictReader(fd)
    for row in dr:
        active_assets_ge += 1
        asset_id = row['Asset Number'].strip()
        details = {
            "desc": row['Asset Description'].strip(),
            "serial": row['Serial Number'].strip(),
            "manufacturer": row['Manufacturer'].strip(),
            "model": row['Model'].strip(),
            # "price": row['price'].strip(),
            # "install": row['install'],
            # "tech_dept": row['tech'],
            # "last_pm": row['lastpm'],
            # "last_cm": row['lastcm'],
            # "department": row['depart'],
            #"site": row['Site'].strip()
            # "div": row['div'],
            # "ge_sys_no": row['ge']
        }
        ge_dic[asset_id] = details

with open(spire_imaging, 'r', encoding='utf-8') as fd:
    dr = csv.DictReader(fd)
    for row in dr:
        active_assets_ge += 1
        asset_id = row['Asset Number'].strip()
        details = {
            "desc": row['Asset Description'].strip(),
            "serial": row['Serial Number'].strip(),
            "manufacturer": row['Manufacturer'].strip(),
            "model": row['Model'].strip(),
            # "price": row['price'].strip(),
            # "install": row['install'],
            # "tech_dept": row['tech'],
            # "last_pm": row['lastpm'],
            # "last_cm": row['lastcm'],
            # "department": row['depart'],
            #"site": row['Site']
            # "div": row['div'],
            # "ge_sys_no": row['ge']
        }
        ge_dic[asset_id] = details

assets_missing = []
assets_missing2 = []

print("Active assets in AssetPlus = " + str(active_assets_ap))
print("Number of assets in IB loader = " + str(active_assets_ge))
print("\nFollowing assets in AssetPlus but the Asset ID not in the Spire IB loader files:")
for key in ap_dic.keys():
    if key not in ge_dic:
        print("{}, {}".format(key, ap_dic[key]))
        assets_missing.append(key)

# for key in ge_dic.keys():
#     if key not in ap_dic:
#         print("Asset ID from IB loader not in AssetPlus = {}".format(key))
#         assets_missing2.append(key)

# # for asset in assets_missing:
# #     print(asset)
# #     print(ap_dic[asset])
#
# print(len(assets_missing2))