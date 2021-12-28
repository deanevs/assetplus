import pandas as pd
import pyodbc
import sys

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)


def chk_empty(str_in):
    if len(str_in) > 0:
        return str_in
    else:
        return ''


def truncate(cursor, cnxn, table):
    print("Truncating: {}".format(table))
    cursor.execute("TRUNCATE TABLE {}".format(table))
    cnxn.commit()


def insert(cursor, cnxn, input_file, table):
    print("Loading: {}".format(table))
    df = pd.read_excel(input_file, sheet_name='MODALITY')
    SQL = "INSERT INTO MODALITY (MOD_CODE, MOD_NAME) VALUES (?,?)"

    cnt = 0
    run_tot = 0
    key_check = []
    for index, row in df.iterrows():
        modality_code = str(int(row['Modality Code']))
        modality_name = str(row['Modality Name'])
        key = (modality_code)
        if key in key_check:
            continue  # skip since already added
        else:
            try:
                cursor.execute(SQL, (modality_code, modality_name))
                key_check.append(key)
                cnt += 1
            except pyodbc.DatabaseError as err:
                print(err)

            if cnt % 1000 == 0:
                run_tot += 1000
                print(str(run_tot))
                cnxn.commit()  # commit every 1000?

    cnxn.commit()
    print("Added {} rows to {}".format(str(cnt), table))


def load(cnxn, input_file, code):
    cursor = cnxn.cursor()
    table_name = 'MODALITY'

    if 'T' in code:  # truncate
        truncate(cursor, cnxn, table_name)
    if 'I' in code:  # insert
        insert(cursor, cnxn, input_file, table_name)
    if 'S' in code:  # skip
        print("\tSkipped {}".format(table_name))







