import pandas as pd
import pyodbc
import sys

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)


def main():
    conn_udi = pyodbc.connect("DSN=PYTHON_UDI")
    conn_ap = pyodbc.connect("DSN=PYTHON_SQL")
    cursor_ap = conn_ap.cursor()

    # $$$$$$$$$$$$$$$$$$ CHECK YOU WANT TO DO THIS $$$$$$$$$$$$$$$$$$$$$$$
    # empty models table since fresh reload
    cursor_ap.execute("TRUNCATE TABLE TYPES")
    conn_ap.commit()

    # fetch UDI devices table
    df_udi = pd.read_sql("SELECT DeviceId, BrandName, VersionModelNumber, CompanyName, DeviceDescription, GMDN_CODE "
                         "FROM MODELS_GMDN", conn_udi)

    # print(df_udi.shape) # (1797711, 6)

    cnt = 0
    run_tot = 0
    key_check = []
    for index, row in df_udi.iterrows():
        udi = str(row['DeviceId'])
        brand = str(row['BrandName']).upper()
        model = str(row['VersionModelNumber']).upper()
        manufacturer = str(row['CompanyName']).upper()[0:50]
        desc = str(row['DeviceDescription']).upper()
        gmdn = str(row['GMDN_CODE'])

        combined = "'UDI: {} ; BRAND: {} ; DESCRIPTION: {}".format(udi, brand, desc)[:1024]  # concatenate fields and limit to 1024 chars

        sql = "INSERT INTO TYPES (TP_TYPE, MARQUE, FOUR_TYPE, CNEH_TYPE, NOM2, ASSET_PART_TYPE, REMP_PRIX," \
              " IS_RFID_TAG) VALUES (?,?,?,?,?,?,?,?)"

        key = (model, manufacturer)  # assetplus uses model & manufacturer as the key for the TYPES
        if key in key_check:
            continue    # skip since already added
        else:
            try:
                cursor_ap.execute(sql, (model, manufacturer, 2, gmdn, combined, 1, 1, 0))
                key_check.append(key)
            except pyodbc.DatabaseError as err:
                print(key)
                # conn_ap.rollback()

            cnt += 1
            if cnt % 1000 == 0:
                run_tot += 1000
                print(str(run_tot))
                conn_ap.commit()    # commit every 1000?

    print("Added {} rows to TYPES ie MODELS".format(str(cnt)))

# map variables to TYPES aka MODELS table
# ap_types_map = {
#     'model':'TP_TYPE',      # version
#     'manufacturer':'MARQUE',    # company
#     'supplier_code':'FOUR_TYPE',    # set=2 'TBD'
#     'gmdn_code':'CNEH_TYPE',    # gmdn_code
#     'name_2':'NOM2',    # brand & prim_DI & description
#     'asset_or_part' : 'ASSET_PART_TYPE', # asset=1, part=2 (set='1')
#     'rep_cost':'REMP_PRIX',  # (set=0)
#     'rfid':'IS_RFID_TAG'   # 0=No, 1=Yes (set='0')
# }


if __name__ == '__main__':
    main()


