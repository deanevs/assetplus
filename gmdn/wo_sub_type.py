import pandas as pd
import pyodbc
import sys

pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)


"""
USAGE: 
1. Edit/add the rows with ******* only
2. Conversion functions added as appropriate
"""

def truncate(cnxn, table):
    print("Truncating: {}".format(table))
    cursor = cnxn.cursor()
    cursor.execute("TRUNCATE TABLE {}".format(table))
    cnxn.commit()


def get_value_str(lst):
    num = len(lst)
    s = ''
    for i in range(num):
        if i == 0 and num > 1:
            s = '(?'
            continue
        if i == 0 and num == 1:
            s = '(?)'
            break
        if i == num - 1:
            s = s + ',?)'
        else:
            s = s + ',?'
    return s

def get_code(subtype):
    dic = {
        'CORRECTIVE': 1,
        'PREVENTATIVE': 3,
        'TECHNICAL ASSISTANCE': 2,
        'WORK': 4,
        'CHECKLIST': 5,
        'TASKS': 6
    }
    return dic[subtype]

def insert(cnxn, input_file, table, fields, sheet_name):
    print("Loading: {}".format(table))
    cursor = cnxn.cursor()
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    fields_adj = '(' + ','.join(fields) + ')'
    SQL =  "INSERT INTO {} {} VALUES {}".format(table, fields_adj, get_value_str(fields))

    cnt = 0
    run_tot = 0
    key_check = []
    for index, row in df.iterrows():
        wo_type = get_code(row['WO TYPE'])                  # **************
        desc = str(row['DESC']).upper()                     # ***************
        args = (wo_type, desc)                              # ******** tuple of all arguments
        key = (wo_type, desc)                               # ***************
        if key in key_check:
            print("Key {} exists!".format(key))
            continue    # skip since already added
        else:
            try:
                cursor.execute(SQL, args)
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
    table_name = 'WO_SUB_TYPE'                              # ***************
    fields = ['WO_TYPE_OPTION', 'SUB_TYPE_DESCRIPTION']     # ***************
    sheet_name = 'WO_SUB_TYPE'                              # ***************

    if 'T' in code:  # truncate
        truncate(cnxn, table_name)
    if 'I' in code:  # insert
        insert(cnxn, input_file, table_name, fields, sheet_name)
    if 'S' in code:  # skip
        print("\tSkipped {}".format(table_name))


