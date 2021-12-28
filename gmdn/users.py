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

def get_value_str(lst):
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
    print("Now loading: {}".format(table))
    cursor = cnxn.cursor()
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    fields_adj = '(' + ','.join(fields) + ')'
    SQL =  "INSERT INTO {} {} VALUES {}".format(table, fields_adj, get_value_str(fields))

    cnt = 0
    run_tot = 0
    key_check = []
    for index, row in df.iterrows():
        user_id = str(row['User'])
        password = str(row['Password'])
        profile = str(row['Profile'])  # MUST EXIST
        change_pwd = row['Change Password']  # 0=no, 1=yes
        user_name = chk_empty(str(row['User Name']))
        email = chk_empty(str(row['Email']))
        rightclick = chk_empty(str(row['Right-click']))
        sql = chk_empty(str(row['Display SQL']))  # 0=Don't show, 1=Show
        args = (user_id,password,profile,change_pwd,user_name,email,rightclick,sql)                             # ******** tuple of all arguments
        key = (user_id)                              # ***************
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
    table_name = 'UTILISAT'                                # ***************
    fields = ['U_ID', 'U_PASSWORD', 'U_ENS_HOSP', 'PSWD_CHANGE_NEXTCNX', 'USER_NAME', 'USER_EMAIL', 'RIGHTCLICK', 'INT_CHAMPREQUETE']                                             # ***************
    sheet_name = 'USERS'                                # ***************

    if 'T' in code:  # truncate
        truncate(cnxn, table_name)
    if 'I' in code:  # insert
        insert(cnxn, input_file, table_name, fields, sheet_name)
    if 'S' in code:  # skip
        print("\tSkipped {}".format(table_name))


