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
        return None

def yes_no(in_str):
    if in_str == 'YES':
        return '1'
    else:
        return '0'

def chk_father(in_str):
    if in_str == 'NONE':
        return ''
    else:
        return "@#@{}@#@".format(in_str)

def main():
    # get our db connection to Assetplus
    server = 'GC0DF7Y2E\SQLEXPRESS'  # for a named instance
    database = 'AP10_9'
    username = 'SOPHIE'
    password = 'SOFLOG'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE='
                          + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # load excel active_assets
    file_to_open = "C:\\Users\\212628255\\Documents\\GE\\AssetPlus\\7 Projects\\GMDN\\2020-07-08 08-11-16_analysis.xlsx"
    df = pd.read_excel(file_to_open)

    # $$$$$$$$$$$$$$$$$$ CHECK YOU WANT TO DO THIS $$$$$$$$$$$$$$$$$$$$$$$
    # empty sites table since fresh reload
    cursor.execute("TRUNCATE TABLE B_EQ1996")
    cursor.commit()
    print("Truncated B_EQ1996")

    cnt = 0
    run_tot = 0
    key_check = []
    # SQL = "INSERT INTO METEIRS (C_METIER, PARENT, CALL_SELECT_FLAG, DISPATCH_PARENT_FLAG, DISPATCH_BROTHER_FLAG, " \
    #       "RESP, AD_EMAIL, PHONE_FIXE, PHONE_MOBILE) VALUES (?,?,?,?,?,?,?,?,?)"

    SQL = "INSERT INTO B_EQ1996 (N_IMMA, PARENT) VALUES (?,?)"
    for index, row in df.iterrows():
        tech_dept = str(row['Technical Department'])
        father = chk_father(str(row['Father']))
        wo_call = yes_no(str(row['WO Call']))
        wo_father = yes_no(str(row['WO Father']))
        wo_peer = yes_no(str(row['WO Peers']))
        manager = chk_empty(str(row['Manager']))
        manager_email = chk_empty(str(row['Manager Email']))
        landline = chk_empty(str(row['Landline']))
        mobile = chk_empty(str(row['Mobile']))
        # hour_cost = chk_empty(row['Hourly Cost'])

        print(tech_dept, father, wo_peer,wo_father,wo_call, manager, manager_email, landline, mobile)

        key = (tech_dept)  # assetplus uses model & manufacturer as the key for the TYPES
        if key in key_check:
            continue    # skip since already added
        else:
            try:
                # cursor.execute(SQL, (tech_dept, father, wo_call, wo_father, wo_peer, manager, manager_email, landline, mobile))
                cursor.execute(SQL, (tech_dept, father))
                key_check.append(key)
            except pyodbc.DatabaseError as err:
                print(err)
                # conn_ap.rollback()

            cnt += 1
            if cnt % 1000 == 0:
                run_tot += 1000
                print(str(run_tot))
                cnxn.commit()    # commit every 1000?
    cnxn.commit()
    print("Added {} rows to METEIRS".format(str(cnt)))


if __name__ == '__main__':
    main()


