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
def convert_str(inp):
    if isinstance(inp, str):
        return inp
    if isinstance(inp, float):
        return str(int(inp))
    else:
        return None

def conv_date_to_str(inp):
    pass


def med_dept_lup(name):
    # return n_uf # med_dept_no
    pass


def supplier_lup(name):
    # return code_four # supplier_code
    pass


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
        asset_id = convert_str(row['Asset Plus Identifier'])
        med_dept_no = 1 # med_dept_lup(row['MD Name'])
        # origin # currently not included
        supp_code = '0112045' # supplier_lup(row['Supplier'])
        manufacturer = str(row['Manufacturer'])
        model = str(row['Model'])
        serial = str(row['Serial No'])
        purch_price = float(row['Price'])
        # install
        # tech_dept_name
        # contract_no
        args = (asset_id, med_dept_no, supp_code, manufacturer, model, serial, purch_price)                         # *************** tuple of all arguments in correct order!
        key = (asset_id)                                # *************** set key
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
    table_name = ''                             # *************** insert table name as string
    fields = ['N_IMMA', 'N_UF', 'CODE_FOUR', 'MARQUE', 'TYP_MOD','N_SERI', 'PRIX']                        # *************** insert the table field names
    sheet_name = 'ASSETS'                             # *************** insert the sheetname from excel

    if 'T' in code:  # truncate
        truncate(cnxn, table_name)
    if 'I' in code:  # insert
        insert(cnxn, input_file, table_name, fields, sheet_name)
    if 'S' in code:  # skip
        print("\tSkipped {}".format(table_name))


