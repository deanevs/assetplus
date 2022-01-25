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


def chk_empty(str_in):
    if len(str_in) > 0:
        return str_in
    else:
        return ''

def set_num_values(lst):
    """
    Helper function to output correct number of ?
    :param lst:
    :return: string eg. (?,?,?,?)
    """
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


def insert(cnxn, input_file, table, fields, sheet_name):
    print("Loading: {}".format(table))
    cursor = cnxn.cursor()
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    fields_adj = '(' + ','.join(fields) + ')'
    SQL =  "INSERT INTO {} {} VALUES {}".format(table, fields_adj, set_num_values(fields))

    cnt = 0
    run_tot = 0
    key_check = []
    for index, row in df.iterrows():
        id = int(row['ID'])
        code = str(row['Code'])
        name = str(row['Name'])   # MUST EXIST
        desc = chk_empty(str(row['Description']))
        args = (id, code, name, desc)                         # *************** tuple of all arguments in correct order!
        key = (id)                                # *************** set key
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

            if cnt % 1000 == 0:     # commit every 1000
                run_tot += 1000
                print(str(run_tot))
                cnxn.commit()

    cnxn.commit()   # commit the total if less than 1000 or the num overflow of last commit
    print("Added {} rows to {}".format(str(cnt), table))

def load(cnxn, input_file, code):
    table_name = 'CUSTOMER'                             # *************** insert table name as string
    fields = ['ID', 'CODE', 'NAME', 'DESCRIPTION']                        # *************** insert the table field names
    sheet_name = 'ORGANISATION'                             # *************** insert the sheetname from excel

    if 'T' in code:  # truncate
        truncate(cnxn, table_name)
    if 'I' in code:  # insert
        insert(cnxn, input_file, table_name, fields, sheet_name)
    if 'S' in code:  # skip
        print("\tSkipped {}".format(table_name))


